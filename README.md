# Soil data plotting

This repository contains scripts for processing and plotting soil data from FA and comparing them to observations ([Sodankylä station](https://litdb.fmi.fi/)).

## Contents
- `soil_data.sh`: Shell script to automate the retrieval of soil data from FA files using the `epygram` package.
- `soil_data_conversion.py`: Script to convert terminal output produced by `soil_data.sh` into txt-format.
- `soil_plot.py`: Script to generate plots for soil temperature and soil moisture from txt/csv files.


## Usage
```
./soil_data.sh 2>&1 | grep -Ev "VisibleDeprecationWarning|masked_value|X002WGI" > input.txt
python3 soil_data_conversion.py
python3 soil_plot.py
```

