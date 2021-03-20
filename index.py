import pandas as pd
from const import FIELDS, SAVE_NAMES, get_archive_names
import os

dirty_path = 'resources/dirty/'

ufs = [uf for uf in os.listdir(dirty_path) if os.path.isdir(dirty_path + uf)]

sidra = pd.read_csv(dirty_path + 'sidra.csv')
sidra['Município'] = [name.split('(')[1][:-1] for name in sidra['Município']]
sidra = sidra.replace('-', 0)
sidra = sidra.drop(columns='Ano de fundação')
sidra.to_csv(dirty_path + 'teste.csv', index=False)

for uf in ufs:
    dirty_uf_path = dirty_path + uf + '/'
    path = 'resources/' + uf + '/'
    cnaes = sidra.loc[sidra['Município'] == uf]
    cnaes = cnaes.drop(columns='Município')
    cities = pd.read_csv(dirty_uf_path + get_archive_names(uf)[0], delimiter=';', encoding='ISO 8859-1')
    cities['Cód.'] = cities['Cod_municipio']
    cities = cities.filter(items=['Cod_municipio', 'Cód.', 'Cod_micro']).groupby('Cod_municipio').max();
    cods = pd.concat([cities, cnaes]).drop_duplicates(keep=False, subset=['Cód.']).index
    cnaes = cnaes.drop(index=cods)
    cnaes = cities.merge(cnaes, how='outer', on='Cód.').drop(columns='Cód.')
    #cnaes = cnaes.groupby('Cod_micro', )
    cnaes.to_csv(path + 'cnaes.csv', index=False);

    if not os.path.isdir(path):
        os.mkdir(path)

    for arch, field, save_name in zip(get_archive_names(uf), FIELDS, SAVE_NAMES):
        data = pd.read_csv(dirty_uf_path + arch, delimiter=';', encoding='ISO 8859-1')
        data = data.filter(items=field)
        data.to_csv(dirty_uf_path + save_name, index=False)

    domicilio1 = pd.read_csv(dirty_uf_path + SAVE_NAMES[1])
    renda = pd.read_csv(dirty_uf_path + SAVE_NAMES[5])
    homem = pd.read_csv(dirty_uf_path + SAVE_NAMES[3])
    mulher = pd.read_csv(dirty_uf_path + SAVE_NAMES[4])
    domicilio1['qtd_dom_coletivo'] = [tot - priv for tot, priv in zip(domicilio1['V001'], domicilio1['V002'])]
    homem = homem.merge(renda[FIELDS[5][0:11]], how='outer', on='Cod_setor', suffixes=('', '_renda'))
    mulher = mulher.merge(renda[[FIELDS[5][0]] + FIELDS[5][11:]], how='outer', on='Cod_setor', suffixes=('', '_renda'))
    homem.to_csv(dirty_uf_path + SAVE_NAMES[3], index=False)
    mulher.to_csv(dirty_uf_path + SAVE_NAMES[4], index=False)
    

    
    