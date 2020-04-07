#!/bin/bash

# 
echo "Downloading data from ourworldindata.org"

echo "https://covid.ourworldindata.org/data/ecdc/full_data.csv"
curl https://covid.ourworldindata.org/data/ecdc/full_data.csv --output ./data/ourworldindata.org/coronavirus-source-data/full_data.csv

echo "https://covid.ourworldindata.org/data/ecdc/locations.csv"
curl https://covid.ourworldindata.org/data/ecdc/locations.csv --output ./data/ourworldindata.org/coronavirus-source-data/locations.csv