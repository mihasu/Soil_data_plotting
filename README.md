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
## Example figures
### Temperature
![Temperature (1)](https://github.com/user-attachments/assets/d5852790-3836-4dea-91dc-b1eeeea5ac8c)

### Moisture
![Moisture (1)](https://github.com/user-attachments/assets/45581e45-477f-498a-969e-11c7fd02e062)




