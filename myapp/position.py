# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 06:20:30 2020

@author: GGuevara
"""

from pvlib import solarposition
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#tz = 'Asia/Calcutta'
#latitude, longitude = 28.6, 77.2
#latitude, longitude, tz = -34, -58, 'America/Argentina/Buenos_Aires'

def sun_position(latitude,longitude,tz):
    
    times = pd.date_range('2019-01-01 00:00:00', '2020-01-01', closed='left',
                          freq='H', tz=tz)
    
    solpos = solarposition.get_solarposition(times, latitude, longitude)
    # remove nighttime
    solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]
    fig, ax = plt.subplots()
    ax = plt.subplot(1, 1, 1, projection='polar')
    
    # draw the analemma loops
    points = ax.scatter(np.radians(solpos.azimuth), solpos.apparent_zenith,
                        s=2, label=None, c=solpos.index.dayofyear)
    ax.figure.colorbar(points)
    
    # draw hour labels
    for hour in np.unique(solpos.index.hour):
        # choose label position by the smallest radius for each hour
        subset = solpos.loc[solpos.index.hour == hour, :]
        r = subset.apparent_zenith
        pos = solpos.loc[r.idxmin(), :]
        ax.text(np.radians(pos['azimuth']), pos['apparent_zenith'], str(hour))
    
    # draw individual days
    for date in pd.to_datetime(['2019-03-21', '2019-06-21', '2019-09-21','2019-12-21']):
        times = pd.date_range(date, date+pd.Timedelta('24h'), freq='5min', tz=tz)
        solpos = solarposition.get_solarposition(times, latitude, longitude)
        solpos = solpos.loc[solpos['apparent_elevation'] > 0, :]
        label = date.strftime('%Y-%m-%d')
        ax.plot(np.radians(solpos.azimuth), solpos.apparent_zenith, label=label)
    
    ax.figure.legend(loc='upper left')
    
    # change coordinates to be like a compass
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(1)
    ax.set_rmax(90)
    
    return ax.figure


#latitude, longitude, tz = -32, -54, 'America/Argentina/Buenos_Aires'
#fig=sun_position(latitude, longitude,tz)
#fig.savefig('fig.png', transparent=True)
