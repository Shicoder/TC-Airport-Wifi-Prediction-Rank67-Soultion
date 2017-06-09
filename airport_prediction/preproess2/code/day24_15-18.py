
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os
import cPickle
###################################### 单个小时求和平均 #############################################
passengers_count_dict={}
time_count_dict = {}
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            date = row[1].split(" ")[0]
            time = int(row[1].split(" ")[1].split(":")[0])#取出小时
            minte= int(row[1].split(" ")[1].split(":")[1][0])
            key = wifi_name_dict[int(file_name.split(".")[0])]+":"+date+"-"+str(time)+"-"+str(minte)
            data = float(row[0])
            if int(time)>=15 and int(time)<=18 and date=='2016-09-18':
                    passengers_count_dict[key] = data
                    print key
    print "writting..."

# time_stamp_dict=[]
# # time_stamp_sublist = []
# for key in passengers_count_dict:
#     time_stamp_sublist=[float(passengers_count_dict[key])/time_count_dict[key],key.split(":")[0],key.split(":")[1]]
#     time_stamp_dict.append(time_stamp_sublist)
#     # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
# f = open("../gbdt_feat/simple_hour_sum.csv", "wb")
# write = csv.writer(f)
# write.writerow(["passengerCount", "wifiap","time"])
# write.writerows(time_stamp_dict)
# f.close()

f = open("../18_val.pkl",'wb')
cPickle.dump(passengers_count_dict,f,-1)
f.close()
