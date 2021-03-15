import pandas as pd
from const import FIELDS, SAVE_NAMES, get_archive_names
import os

ufs = os.listdir('resources/dirty')

for uf in ufs:
    dirty_path = 'resources/dirty/' + uf + '/'
    path = 'resources/' + uf

    if not os.path.isdir(path):
        os.mkdir(path)

    for arch, field, save_name in zip(get_archive_names(uf), FIELDS, SAVE_NAMES):
        data = pd.read_csv(dirty_path + arch, delimiter=';', encoding='ISO 8859-1')
        data = data.filter(items=field)
        data.to_csv(dirty_path + save_name, index=False)

    domicilio1 = pd.read_csv(dirty_path + SAVE_NAMES[1])
    domicilio1['qtd_dom_coletivo'] = [tot - priv for tot, priv in zip(domicilio1['V001'], domicilio1['V002'])]
    domicilio1.to_csv(dirty_path + SAVE_NAMES[1], index=False)
    