#!/usr/bin/bash

#echo "Loading Prices Data"
#python3 preprocess/load_prices_data.py

echo "Starting Data Preprocessing"
Rscript preprocess/preprocess.R
#echo "Starting Feature Engineering"
#python3 preprocess/feature_engineering.py
#echo "Starting Feature Selection"
#Rscript preprocess/feature_selection.R
#echo "Done!"

#echo "Starting Data Preprocessing"
#Rscript preprocess/TS_preprocess.R
#echo "Starting Feature Engineering"
#python3 preprocess/TS_feature_engineering.py
#echo "Done!"