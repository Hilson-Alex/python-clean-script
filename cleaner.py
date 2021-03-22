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
    income_man = income[FIELDS[5][0:11]]
    income_woman = income[[FIELDS[5][0]] + FIELDS[5][11:]]
    return [sex.merge(inc, how='outer', on='Cod_setor', suffixes=('','_renda')) 
            for sex, inc in zip([man, woman], [income_man, income_woman])]