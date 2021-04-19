import pandas as pd
from const import FIELDS, SAVE_NAMES, get_archive_names
import os, shutil, sys
from cleaner import aggregate, sidra_clean, divide_income

# res_path = sys.argv[1]
res_path = 'resources/'
if (len(sys.argv) > 1 ):
    res_path = sys.argv[1]

dirty_path = res_path + 'dirty/'

ufs = [uf for uf in os.listdir(dirty_path) if os.path.isdir(dirty_path + uf)]

sidra = pd.read_csv(dirty_path + 'sidra.csv')
sidra.loc[:,'Município'] = [name.split('(')[1][:-1] for name in sidra['Município']]
sidra = sidra.replace('-', 0)
sidra.to_csv(dirty_path + 'cnaes.csv', index=False)
sidra = pd.read_csv(dirty_path + 'cnaes.csv')

for uf in ufs:
    
    # declaração de variáveis
    dirty_uf_path = dirty_path + uf + '/'
    path = res_path + uf + '/'
    archs = get_archive_names(uf)

    if not os.path.isdir(path):
        os.mkdir(path)

    # separação e limpeza do sidra
    cnaes = sidra.loc[sidra['Município'] == uf]
    cities = pd.read_csv(dirty_uf_path + archs[0], delimiter=';', encoding='ISO 8859-1')
    sidra_clean(cnaes, cities).to_csv(path + 'cnaes.csv', index=False)

    #criação de tabelas intermediárias
    for arch, field, save_name in zip(archs, FIELDS, SAVE_NAMES):
        data = pd.read_csv(dirty_uf_path + arch, delimiter=';', encoding='ISO 8859-1')
        data = data.filter(items=field)
        data = data.replace('X', '')
        data.to_csv(dirty_uf_path + save_name, index=False)

    midtables = [pd.read_csv(dirty_uf_path + table) for table in SAVE_NAMES]

    # composição de campos e mescla de tabelas
    midtables[1].loc[:,'qtd_dom_coletivo'] = [tot - priv for tot, priv in zip(midtables[1]['V001'], midtables[1]['V002'])]
    midtables[3], midtables[4] = divide_income(midtables[3], midtables[4], midtables[5])

    for arch, name in zip(midtables[1:], SAVE_NAMES[1:-1]):
        aggregate(midtables[0], arch, FIELDS[0][1], FIELDS[0][:2]).to_csv(path + name, index=False)

    midtables[0] = midtables[0].drop(columns=FIELDS[0][0]).groupby(FIELDS[0][1], as_index=False).max()
    midtables[0].to_csv(path + SAVE_NAMES[0], index=False)

    print ("Limpeza das tabelas do estado de " + uf + " Terminada.")

print ("Fim da limpeza.")