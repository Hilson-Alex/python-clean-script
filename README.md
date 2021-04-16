# python-clean-script

Are you not a portuguese speaker? Read this in [english](/README.en.md)

Este é um script em python para limpeza das tabelas do censo de 2010 do IBGE (Instituto Brasileiro de Geografia Estatística) para uma simulação da população brasileira e como uma epidemia se espalharia em microrregiões das terras tupiniquins.

O IBGE coleta e fornece dados tanto sobre regiões brasileiras (bairros, cidades, microrregiões, estados, etc...) quanto sobre o povo brasileiro para estúdos estatísticos, e esperamos usar estes dados para criar agentes inteligentes capazes de simular a população local durante uma epidemia.

> Para deixar o mais claro possível: Estes dados são **públicos** e não há dados sensíveis nestas tabelas.
> As tabelas, exceto a de CNAEs podem ser encontradas [aqui](https://www.ibge.gov.br/estatisticas/sociais/populacao/9662-censo-demografico-2010.html?edicao=10410&t=resultados)
> A tabela de CNAEs pode ser encontrada [aqui](https://sidra.ibge.gov.br/Tabela/993)

Este algoritmo, muito provavelmente **não** é útil para outros repositórios que não seja o nosso, foi feito especificamente para o nosso projeto, mas o deixaremos público para manter a pesquisa o mais transparente possível, visto que ele foi completamente pago com dinheiro público, então concordamos que seus resultados devem ser públicos também.

## Modo de uso

Como dito anteriormente, este algoritmo é uma pequena parte de um projeto maior, o que o torna um repositório extremamente específico. Mas, se você pretende rodá-lo em seu computador por alguma razão, siga estes passos:

### Pré-requisitos

O único pré-requisito é a biblioteca pandas que usamos para manipulação de arquivos CSV. Para baixá-la, apenas rode o comando abaixo no terminal:

```bash
pip install pandas
```

### Instalação

Para ter uma cópia deste projeto, apenas clone-o em seu computador usando ```git clone``` ou ```git submodule add``` para colocá-lo como um submódulo em seu repositório.

### Rodando

Para usar este script, você deve ter uma pasta para arquivos externos (resources), e dentro desta pasta, uma pasta com nome "dirty" com as tabelas do IBGE. O diretório de se parecer com isso:

```bash
resources
├───dirty
│   └───UF
```

Dentro da pasta "dirty", você pode ter pastas de um ou mais estados com o nome da UF do estado (SC, RS, MG, etc..) e com as tabelas do censo no formato CSV dentro destas pastas. 
Também é necessária uma [Tabela Sidra](https://sidra.ibge.gov.br/Tabela/993) no diretório "dirty" sem a documentação no final do arquivo nem com os headers no começo.

Tendo estes arquivos, apenas rode:
```bash
python caminho/para/python-clean-script/index.py caminho/para/resources/
```

E o algoritmo limpará as tabelas.

## Authores
- Gabriel Assunção de Souza: [@Souza-gabriel](https://github.com/Souza-gabriel)
- Hilson A. W. Jr.: [@Hilson-Alex](https://github.com/Hilson-Alex)
