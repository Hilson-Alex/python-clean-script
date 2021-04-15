import pandas as pd
from const import FIELDS

def aggregate (left, right, field_agg, fields):
    left = left.filter(items=fields)
    right = left.merge(right, how='outer', on=fields[0]).drop(columns=fields[0])
    return right.groupby(field_agg, as_index=False).sum()


def sidra_clean (cnaes, cities):
    cnaes = cnaes.drop(columns='Município')
    cities['Cód.'] = cities['Cod_municipio']
    cities = cities.filter(items=['Cod_municipio', 'Cód.', 'Cod_micro']).groupby('Cod_municipio').max()
    cods = pd.concat([cities, cnaes]).drop_duplicates(keep=False, subset=['Cód.']).index
    cnaes = cnaes.drop(index=cods)
    return aggregate(cities, cnaes, 'Cod_micro', ['Cód.', 'Cod_micro'])


def divide_income (man, woman, income):
    columns = FIELDS[5]
    income_man = income.loc[:,columns[0:11]]
    income_woman = income.loc[:,[columns[0]] + columns[11:]]
    arr = []
    for income in [income_man, income_woman]:
        columns = income.columns
        income.loc[:,'Classe E'] = income[columns[1]] + income[columns[2]] + income[columns[3]] 
        + income[columns[10]]
        income.loc[:,'Classe D'] = income[columns[4]] + income[columns[5]]
        income.loc[:,'Classe C'] = income[columns[6]]
        income.loc[:,'Classe B'] = income[columns[7]] + income[columns[8]]
        income.loc[:,'Classe A'] = income[columns[9]]
        arr.append(income.drop(columns=columns[1:11]))
    
    return [sex.merge(inc, how='outer', on='Cod_setor', suffixes=('','_renda')) 
            for sex, inc in zip([man, woman], arr)]