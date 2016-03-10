from pydap.client import open_url
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
import sys

def get_data(var_id, row, col):

    base_url = ('http://dapds00.nci.org.au/thredds/dodsC/rr9/Climate/eMAST/'
           'ANUClimate/0_01deg/v1m0_aus/mon/land/%s/e_01/1970_2012/' % (var_id))
    emast_id = "eMAST_ANUClimate_mon_tmax_v1m0"
    start_date = "1970-01-01"
    stop_date = "2000-12-31"

    current = datetime.strptime(start_date, "%Y-%m-%d")
    stop = datetime.strptime(stop_date, "%Y-%m-%d")

    tmax = []
    dates = []
    while current < stop:
        
        if current.month < 10:
            month = "0%s" % (current.month)
        else:
            month = "%s" % (current.month)
        year = current.year

        url = "%s%s_%s%s.nc" % (base_url, emast_id, year, month)

        dataset = open_url(url)
        variable = dataset['air_temperature']
        tmax.append(variable[0,2000,2000].array[:][0][0][0])
        dates.append(current)

        current += relativedelta(months=1)

    f = open("tmax_%d_%d.txt" % (row, col), "w")
    for i in xrange(tmax):
        f >> tmax
    f.close()

var_id = "tmax"
row = 2000
col = 2000
get_data(var_id, row, col)
