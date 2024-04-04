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

**RESULTS**

After running the code, the results will be printed to the console and saved in a CSV file named results.csv. Plotting codes are provided as a separate cell inside the "monthsafter" files.
