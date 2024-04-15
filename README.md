**HEATWAVE ANALYSIS**

This repository contains Python code for analyzing oceanographic and biological data, focusing on variables such as Sea Surface Temperature (SST), Sea-air flux ​(fgco2), pH, Aragonite Saturation, Surface partial pressure of carbon dioxide in sea water (spco2), Alkalinity, Chlorophyll, Wind Speed and Wind Direction.

**GETTING STARTED**

To run the code in this repository, follow the instructions below:

**PRE-REQUISITES**

Python

Required Python libraries: numpy, pandas, netCDF4, scipy, xarray, matplotlib, docx

**CONFIGURATION**

You may need to modify the following parameters in the "PARAMETERS.csv" file:

start_year: Start year of the analysis period

end_year: End year of the analysis period

region_name: Name of the region

longhurst_region_code: Code representing the Longhurst region

combined_cat_values: List of values representing categories

consecutive_months_threshold: Threshold for consecutive months

months_after: Number of months after a consecutive period

num_samples: Number of samples for statistical analysis

**NOTEBOOKS OVERVIEW**

This repository contains notebooks for conducting statistical analysis on heatwave data to investigate the significance of oceanographic and biological variables during consecutive heatwave periods compared to non-heatwave periods. For each oceanographic variables and biological variables, there are two sets of notebooks named "consecutive" and "months_after". The Consecutive notebook provides the result for statistical analysis of variables which existed for 'n' number of consective months. And if you want to find out what happened to each variable after each months when a heatwave existed consecutively for 'n' months, "months_after" notebooks should be used.

1. Preprocessing.ipynb
   
Inputs:

The notebook takes input parameters from a CSV file (PARAMETERS.csv) containing information such as start year, end year, Longhurst region code, region name, number of samples, consecutive months threshold, and months after.

Outputs:

The notebook performs preprocessing steps on data stored in netCDF files.

Outputs include:

Sliced heatwave data for the specified time range saved as new netCDF files.

Masked heatwave data based on Longhurst regions saved as netCDF files.

Monthly masks for marine heatwaves saved as netCDF files.

Consecutive monthly masks for values 3 or 4 saved as netCDF files.

Information about consecutive heatwaves saved as CSV files.

2. Statistical_Analysis.ipynb

Inputs:

The notebook takes preprocessed heatwave data, Longhurst region masks, and specified parameters for statistical analysis.

Outputs:

Performs statistical analysis using the Wilcoxon signed-rank test to compare variables during consecutive heatwave periods and non-heatwave periods.
CSV files containing results of the statistical analysis for each variable. Plots are created in the upcoming cells.
