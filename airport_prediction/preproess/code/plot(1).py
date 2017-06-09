__author__ = 'shi'
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pylab as plt
import test_stationarity
series_list={}
#####################################################################################
"""
for i in range(749):
    df = pd.read_csv("../merge_10/"+str(i+1)+".csv",index_col="timeStamp")
    # df = pd.read_csv("../merge_10_check/checkin.csv",index_col="timeStamp")
    df.index = pd.to_datetime(df.index)
    ts = df['passengerCount']
    series_list[i]=ts
    # print ts.head()
    # print ts.head().index
    # print df.describe()
    # print df.dtypes
# print "check date :",ts['2016-09-10 08:58:02'],ts['2016-09-10'],"http://www.cnblogs.com/foley/p/5582358.html"
"""
#log_tran
"""
# ts_log = np.log(ts)
test_stationarity.draw_ts(series_list)
"""
##########################################################################
# for i in range(480):
#     print i+1
#     df1 = pd.read_csv("../merge_10/"+str(i+1)+".csv",index_col="timeStamp")
#     # df = pd.read_csv("../merge_10_check/checkin.csv",index_col="timeStamp")
#     df1.index = pd.to_datetime(df1.index)
#     ts1 = df1['passengerCount']
#     test_stationarity.draw_ts1(ts1)
########################################### test ###############################
df1 = pd.read_csv("../merge_10/103.csv",index_col="timeStamp")
# df = pd.read_csv("../merge_10_check/checkin.csv",index_col="timeStamp")

ts1 = df1['passengerCount']
test_stationarity.draw_ts1(ts1)
###############################################
# df = pd.read_csv("../submit/airport_gz_passenger_predict_dict_put_into_cricle_not_delete_0911.csv")
# # df = pd.read_csv("../merge_10_check/checkin.csv",index_col="timeStamp")
# ts = df['passengercount']
# print "not have 0911",df.describe()
# series_list[0]=ts
# df = pd.read_csv("../submit/airport_gz_passenger_predict_dict_put_into_cricle.csv")
# ts = df['passengercount']
# print " have 0911",df.describe()
# series_list[0]=ts
# test_stationarity.draw_ts1(ts)
# df = pd.read_csv("../merge_10_check/checkin.csv")
# ts = df['passengerCount']
# print "cricle out",df.describe()
# series_list[1]=ts
# test_stationarity.draw_ts1(ts)
################################################################################
"""b. smooth"""

# test_stationarity.draw_trend(ts_log,12)