# python-clean-script

Read this in [english](/README.en.md)

This is a python script for cleaning IBGE census tables for an simulation of Brazil local population and how an epidemy would spread in certain brazilian regions.

IBGE is a brazilian Institute that collect and provide data about Brazil regions (states, cities, etc...) and brazilian people for estatistics purposes, 
and we hope to use this data to create intelligent agents to simulate a local population during an epidemy.

This code is **not** useful for other repositories, it's made especifically for our project, but We'll let then public for transparency purposes, keeping in mind that
this research was paid with public money, and so, we think that the results may be public too.

## Getting Started

As told before, this is a small part of a bigger project, and is an extremely especific repository, but, if you want to get it running in your machine for some reason
just follow this steps.

### Prerequisites

The only prerequisite for this project is the Pandas library, that we used to handle csv data. To install it, just run the code bellow in the terminal:

```bash
pip install pandas
```

### Instalation

To have a copy of this script running you just need to clone it in your computer using ```git clone``` or ```git submodule add```.

### Running

To use this you must have an folder for resources, and inside this folder, a folder "dirty"  with the IBGE Tables. The directory must look like this:

```bash
resources
├───dirty
│   └───UF
```

Inside the dirty folder you can have one or more UF folder with the brazilan states UF as a name and the IBGE census tables inside it. 
You'll also need an [Sidra Table](https://sidra.ibge.gov.br/Tabela/993) in the dirty directory without the documentation in the final of the file and without
the headers on the beggining

After this, you just run :
```bash
python path/to/python-clean-script/index.py path/to/resources/
```

And the script will clean the tables.

## Authors
- Gabriel Assunção de Souza: [@Souza-gabriel](https://github.com/Souza-gabriel)
- Hilson A. W. Jr.: [@Hilson-Alex](https://github.com/Hilson-Alex)
