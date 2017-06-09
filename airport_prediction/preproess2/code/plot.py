__author__ = 'shi'
# -*- coding:utf-8 -*-

import numpy as np
import pandas as pd
import cPickle
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
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
# import os
# direction = "../merge_10_add_predict/"
# file_list = os.listdir(direction)
# for file_name in file_list:
#     print wifi_name_dict[int(file_name.split(".")[0])]
#     file_path = direction+file_name
#     df1 = pd.read_csv(file_path,index_col="timeStamp")
#     # df = pd.read_csv("../merge_10_check/checkin.csv",index_col="timeStamp")
#     df1.index = pd.to_datetime(df1.index)
#     df1.sort_index(inplace=True)
#     # cols = list(df1)
#     # cols.insert(0,cols.pop(cols.index('passengerCount')))
#     # df1=df1.ix[:,cols]
#     # rol_mean=pd.ewma(df1,span=3)
#     # rol_mean.to_csv("../merge_10_meidian/"+file_name)
#     ts1 = df1['passengerCount']
#     # test_stationarity.draw_trend(ts1,9)
#     test_stationarity.draw_ts1(ts1)
########################################### test ###############################
df1 = pd.read_csv("../merge_10/479.csv",index_col="timeStamp")
# df = pd.read_csv("../merge_10_check/checkin.csv",index_col="timeStamp")
df1.index = pd.to_datetime(df1.index)
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