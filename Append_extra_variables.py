#!/usr/bin/env python3
"""
Created by Daniel J. Ford (d.ford@exeter.ac.uk)
Date: 03/2023

"""

import os
import sys
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt
os.chdir('C:\\Users\\df391\\OneDrive - University of Exeter\\Post_Doc_ESA_Contract\\OceanICU')

print(os.getcwd())
print(os.path.join(os.getcwd(),'Data_Loading'))

sys.path.append(os.path.join(os.getcwd(),'Data_Loading'))
sys.path.append(os.path.join(os.getcwd()))
import data_utils as du
"""
"""
wind_file = 'E:/OceanHealth/CCMP_v3.1_wind.nc'
wind_file_era = 'E:/OceanHealth/ERA5_wind.nc'
chl_file = 'E:/OceanHealth/OC-CCI_chlor_a.nc'


def append_variables(file,start_yr,end_yr,log,lag,dims = ('time','lat','lon'),trans = [2,1,0]):
    import construct_input_netcdf as cinp

    import Data_Loading.ERA5_data_download as era5
    era5.era5_average('F:/Data/ERA5/DAILY/monthly','E:/OceanHealth/ERA5',start_yr=start_yr,end_yr=end_yr,log = log,lag=lag,var='ws')

    vars = [['ERA5','ws',os.path.join('E:/OceanHealth/ERA5','%Y','%Y_%m*.nc'),0]]

    cinp.driver(wind_file_era,vars,start_yr = start_yr,end_yr = end_yr,lon = log,lat = lag,fill_clim=False)

    c = Dataset(wind_file_era,'r')
    chl = np.array(c['ERA5_ws'])
    c.close()
    chl = np.transpose(chl,trans)
    c = Dataset(file,'a')
    if 'ERA5_ws' in c.variables.keys():
        c.variables['ERA5_ws'][:] = chl
    else:
        outs = c.createVariable('ERA5_ws','f4',dims)
        outs[:] = chl
    c.close()

    import Data_Loading.ccmp_average as cc
    cc.ccmp_average('F:/Data/CCMP/v3.1/monthly',outloc='E:/OceanHealth/CCMP',start_yr=start_yr,end_yr=end_yr,log=log,lag=lag,v =3.1,var='ws',geb_file='F:/Data/Bathymetry/GEBCO_2023.nc')


    # #Vars should have each entry as [Extra_Name, netcdf_variable_name,data_location,produce_anomaly]
    vars = [['CCMP','ws',os.path.join('E:/OceanHealth/CCMP','%Y','CCMP_3.1_ws_%Y%m*.nc'),0]]
    # ['CCMP','v',os.path.join('D:/Support/Sayooj/CCMP_v3.0/1DEG','%Y','%Y_%m*v.nc'),0],
    # ['CCMP','u',os.path.join('D:/Support/Sayooj/CCMP_v3.0/1DEG','%Y','%Y_%m*u.nc'),0]
    # ]


    cinp.driver(wind_file,vars,start_yr = start_yr,end_yr = end_yr,lon = log,lat = lag,fill_clim=False)

    c = Dataset(wind_file,'r')
    wind = np.array(c['CCMP_ws'])
    c.close()
    wind = np.transpose(wind,trans)
    c = Dataset(file,'a')
    if 'CCMP_ws' in c.variables.keys():
        c.variables['CCMP_ws'][:] = wind
    else:
        outs = c.createVariable('CCMP_ws','f4',dims)
        outs[:] = wind
    c.close()
    #

    import Data_Loading.CCI_OC_SPATIAL_AV as oc
    oc.oc_cci_average('F:\Data\OC-CCI\monthly\chlor_a',out_folder='E:/OceanHealth/OC-CCI',start_yr=start_yr,end_yr=end_yr,log=log,lag=lag,conv=True,area_wei=True)
    vars = [['OC-CCI','chlor_a',os.path.join('E:/OceanHealth/OC-CCI','%Y','%Y_%m*.nc'),0]
    ]
    cinp.driver(chl_file,vars,start_yr = start_yr,end_yr = end_yr,lon = log,lat = lag,fill_clim=False)
    c = Dataset(chl_file,'r')
    chl = np.array(c['OC-CCI_chlor_a'])
    c.close()
    chl = np.transpose(chl,trans)
    chl = np.log10(chl)
    c = Dataset(file,'a')
    if 'OC-CCI_chlor_a' in c.variables.keys():
        c.variables['OC-CCI_chlor_a'][:] = chl
    else:
        outs = c.createVariable('OC-CCI_chlor_a','f4',dims)
        outs[:] = chl
    c.close()

# oceansoda_file = 'E:/OceanHealth/OceanSODA_ETHZ-v2023.OCADS.01_1982-2022+DF.nc'
# start_yr_o = 1982
# end_yr_o = 2022
# log,lag = du.reg_grid(lat=1,lon=1)
#
# append_variables(oceansoda_file,start_yr_o,end_yr_o,log,lag)
#
oceansoda_file = 'E:/OceanHealth/Ford_et_al_UExP-FNN-U_physics_carbonatesystem_ESASCOPE_v5.nc'
start_yr_o = 1985
end_yr_o = 2023
log,lag = du.reg_grid(lat=1,lon=1)

append_variables(oceansoda_file,start_yr_o,end_yr_o,log,lag,dims=('longitude','latitude','time'),trans=[0,1,2])

# oceansoda_file = 'E:/OceanHealth/UExP-FNN-U_GCB2024.nc'
# start_yr_o = 1985
# end_yr_o = 2023
# log,lag = du.reg_grid(lat=1,lon=1)
#
# append_variables(oceansoda_file,start_yr_o,end_yr_o,log,lag,dims=('longitude','latitude','time'),trans=[0,1,2])
