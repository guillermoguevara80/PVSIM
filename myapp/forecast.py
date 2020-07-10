# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 22:03:43 2020

@author: GGuevara
"""


from pandas import Timedelta, Timestamp
import matplotlib.pyplot as plt
import datetime

# import pvlib forecast models
from pvlib.forecast import GFS, NAM, NDFD, HRRR, RAP

# specify location (Tucson, AZ)

def forecast(latitude, longitude, tz='UTC'):
    # specify time range.
    start = Timestamp(datetime.date.today(), tz=tz)
    
    end = start + Timedelta(days=7)
    
    irrad_vars = ['ghi', 'dni', 'dhi']
    
    # 0.25 deg available
    model = GFS()
    
    # retrieve data. returns pandas.DataFrame object
    raw_data = model.get_data(latitude, longitude, start, end)
    
    #print(raw_data.head())
    
    data = raw_data
    data=data.resample('15min').asfreq()
    data=data.interpolate(method='linear', limit_direction='forward', axis=0)
    
    # rename the columns according the key/value pairs in model.variables.
    data = model.rename(data)
    
    # convert temperature
    data['temp_air'] = model.kelvin_to_celsius(data['temp_air'])
    
    # convert wind components to wind speed
    data['wind_speed'] = model.uv_to_speed(data)
    
    # calculate irradiance estimates from cloud cover.
    # uses a cloud_cover to ghi to dni model or a
    # uses a cloud cover to transmittance to irradiance model.
    # this step is discussed in more detail in the next section
    irrad_data = model.cloud_cover_to_irradiance(data['total_clouds'])
    
    data = data.join(irrad_data, how='outer')
    
    # keep only the final data
    data = data[model.output_variables]
    fig=data[['ghi', 'dni', 'dhi']].plot().get_figure()
    return fig    
    
    
#latitude, longitude, tz = -34, -58, 'America/Argentina/Buenos_Aires'
#fig=forecast(latitude, longitude, tz)
#fig.savefig('irradiance.png')