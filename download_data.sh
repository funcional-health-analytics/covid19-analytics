#!/bin/bash

# 
echo "Downloading data from ourworldindata.org"

echo "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
curl https://covid.ourworldindata.org/data/ecdc/full_data.csv --output ./data/ourworldindata.org/coronavirus-source-data/full_data.csv

echo "https://covid.ourworldindata.org/data/ecdc/locations.csv"
curl https://covid.ourworldindata.org/data/ecdc/locations.csv --output ./data/ourworldindata.org/coronavirus-source-data/locations.csv

echo ""
echo "Downloading data from World Bank"

echo "http://databank.worldbank.org/data/download/WDI_csv.zip"
rm ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/WDI_csv.zip
wget http://databank.worldbank.org/data/download/WDI_csv.zip -P ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/
unzip -o ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/WDI_csv.zip -d ./data/large/datacatalog.worldbank.org/dataset/world-development-indicators/