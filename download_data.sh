#!/bin/bash

# 
echo "**** Downloading data from ourworldindata.org ****"

echo "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
curl https://covid.ourworldindata.org/data/ecdc/full_data.csv --output ./data/ourworldindata.org/coronavirus-source-data/full_data.csv

echo "https://covid.ourworldindata.org/data/ecdc/locations.csv"
curl https://covid.ourworldindata.org/data/ecdc/locations.csv --output ./data/ourworldindata.org/coronavirus-source-data/locations.csv


echo ""
echo "**** Downloading data from Brasil.io ****"

echo "https://data.brasil.io/dataset/covid19/caso_full.csv.gz"
curl https://data.brasil.io/dataset/covid19/caso_full.csv.gz --output ./data/brasil.io/dataset/covid19/caso_full.csv.gz
gunzip ./data/brasil.io/dataset/covid19/caso_full.csv.gz -f

echo ""
echo "**** Downloading data from World Bank ****"

echo "http://databank.worldbank.org/data/download/WDI_csv.zip"
rm ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/WDI_csv.zip
wget http://databank.worldbank.org/data/download/WDI_csv.zip -P ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/
unzip -o ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/WDI_csv.zip -d ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/

echo "**** Downloading data SRAG data (from official Fiocruz repository) ****"

#echo "https://raw.githubusercontent.com/belisards/srag_brasil/master/data/casos_br.csv"
#curl https://raw.githubusercontent.com/belisards/srag_brasil/master/data/casos_br.csv --output ./data/srag_brasil/casos_br.csv

echo "https://gitlab.procc.fiocruz.br/mave/repo/-/raw/master/Dados/InfoGripe/dados_semanais_faixa_etaria_sexo_virus_sem_filtro_sintomas.csv"
curl https://gitlab.procc.fiocruz.br/mave/repo/-/raw/master/Dados/InfoGripe/dados_semanais_faixa_etaria_sexo_virus_sem_filtro_sintomas.csv --output ./data/large/fiocruz/infogripe/dados_semanais_faixa_etaria_sexo_virus_sem_filtro_sintomas.csv

echo "https://gitlab.procc.fiocruz.br/mave/repo/-/raw/master/Dados/InfoGripe/dados_semanais_faixa_etaria_sexo_virus.csv"
curl https://gitlab.procc.fiocruz.br/mave/repo/-/raw/master/Dados/InfoGripe/dados_semanais_faixa_etaria_sexo_virus.csv --output ./data/large/fiocruz/infogripe/dados_semanais_faixa_etaria_sexo_virus.csv
