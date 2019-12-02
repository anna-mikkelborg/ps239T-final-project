# Import required libraries
import pandas as pd
import time

# pytrends is an unofficial Google Trends API
from pytrends.request import TrendReq

# connect with Google Trends
pytrend = TrendReq(hl='en-US', tz=360)

# create empty data frames
interest_by_region_whm = pd.DataFrame()
interest_by_region_weather = pd.DataFrame()
interest_by_region_whmweather = pd.DataFrame()

# query Google Trends 100 times
for i in range(100):
    # get search rates for "White History Month" and add to appropriate data frame
    pytrend.build_payload(['white history month'], timeframe='all', geo='US')
    df1 = pytrend.interest_by_region(resolution ='DMA', inc_low_vol=True, inc_geo_code=False)
    interest_by_region_whm = df1.append(interest_by_region_whm)
    # get search rates for "weather" and add to appropriate data frame
    pytrend.build_payload(['weather'], timeframe='all', geo='US')
    df2 = pytrend.interest_by_region(resolution='DMA',inc_low_vol=True, inc_geo_code=False)
    interest_by_region_weather = df2.append(interest_by_region_weather)
    # get search rates for "weather + 'White History Month'" and add to appropriate data frame
    pytrend.build_payload(['weather + \'white history month\''], timeframe='all', geo='US')
    df3 = pytrend.interest_by_region(resolution='DMA', inc_low_vol=True, inc_geo_code=False)
    interest_by_region_whmweather = df3.append(interest_by_region_whmweather)
    # wait 1 second before next query
    time.sleep(1)
    
# convert index to column titled "region"
interest_by_region_whm['region'] = interest_by_region_whm.index
interest_by_region_weather['region'] = interest_by_region_weather.index
interest_by_region_whmweather['region'] = interest_by_region_whmweather.index

# write .csvs
interest_by_region_whm.to_csv (r'/Users/anna/Desktop/239T_materials/239T-final-project/whm.csv', index = None, header=True)
interest_by_region_weather.to_csv (r'/Users/anna/Desktop/239T_materials/239T-final-project/weather.csv', index = None, header=True)
interest_by_region_whmweather.to_csv (r'/Users/anna/Desktop/239T_materials/239T-final-project/whmweather.csv', index = None, header=True)
