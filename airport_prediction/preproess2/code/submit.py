__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os
import cPickle
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))

# direction = "../result_simple_dot_mean/"
direction = "../win_9_day(19_24)_test/"
file_list = os.listdir(direction)
result_list = []
for file_name in file_list:
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
        # one_result = row[0],wifi_name_dict[file_name]
        pre_date="2016-09-24-"
        time_stamp1 = row[1].split(":")[0]
        time_stamp2 = row[1].split(":")[1][0:1]
        gang='-'
        pre_date+=time_stamp1
        pre_date+=gang
        pre_date+=time_stamp2
        one_result = [row[0],wifi_name_dict[int(file_name.split(".")[0])],pre_date]
        result_list.append(one_result)

print "writting..."
# f = open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv", "wb")
f = open("../submit/airport_gz_passenger_predict_offline_win9_allday.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
write.writerows(result_list)
f.close()