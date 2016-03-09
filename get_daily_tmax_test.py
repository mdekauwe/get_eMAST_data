from pydap.client import open_url
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import sys

var_id = "tmax"
url = ('http://dapds00.nci.org.au/thredds/dodsC/rr9/Climate/eMAST/'
       'ANUClimate/0_01deg/v1m0_aus/day/land/%s/e_01' % (var_id))
emast_id = "eMAST_ANUClimate_day"
start_date = "1970-01-01"
stop_date = "1970-12-31"

current = datetime.strptime(start_date, "%Y-%m-%d")
stop = datetime.strptime(stop_date, "%Y-%m-%d")

tmax = []
dates = []
while current < stop:

    if current.day < 10:
        day = "0%s" % (current.day)
    else:
        day = "%s" % (current.day)
    if current.month < 10:
        month = "0%s" % (current.month)
    else:
        month = "%s" % (current.month)
    year = current.year

    date_str = "%s%s%s" % (year, month, day)
    doy_url = "%s/%d/%s_%s_v1m0_%s.nc" % (url, year, emast_id, var_id, date_str)
    dataset = open_url(doy_url)
    variable = dataset['air_temperature']
    tmax.append(variable[0,2000,2000].array[:][0][0][0])
    dates.append(current)

    current += timedelta(days=1)
