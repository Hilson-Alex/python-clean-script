
FIELDS = [
    ['Cod_setor', 'Cod_micro', 'Nome_da_micro'],

    ['Cod_setor'] + ['V' + str(n).zfill(3) for n in range(1, 6)] + 
    ['V' + str(n).zfill(3) for n in range(50, 60)],

    ['Cod_setor'] + ['V' + str(n).zfill(3) for n in range(3, 6)],

    ['Cod_setor', 'V001', 'V019', 'V021', 'V022'] + 
    ['V' + str(n).zfill(3) for n in range(35, 135)],

    ['Cod_setor', 'V001', 'V019', 'V021', 'V022'] + 
    ['V' + str(n).zfill(3) for n in range(35, 135)],

    ['Cod_setor'] + ['V' + str(n).zfill(3) for n in range(23, 33)] +
    ['V' + str(n).zfill(3) for n in range(45, 55)],
]

SAVE_NAMES = [
        'basico_clean.csv',
        'domicilio1_clean.csv',
        'domicilio2_clean.csv',
        'pessoa11_clean.csv',
        'pessoa12_clean.csv',
        'pessoaRenda_clean.csv'
    ]


def get_archive_names(uf):
    return [
        'Basico_' + uf + '.csv',
        'Domicilio01_' + uf + '.csv',
        'Domicilio02_' + uf + '.csv',
        'Pessoa11_' + uf + '.csv',
        'Pessoa12_' + uf + '.csv',
        'PessoaRenda_' + uf + '.csv'
    ]