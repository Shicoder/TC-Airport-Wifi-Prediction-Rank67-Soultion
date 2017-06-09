
#-*-coding:utf-8-*-
import csv
import pandas as pd
import os
import cPickle
###################################### ��������Сʱ���ƽ�� ####################################
passengers_count_dict={}
time_count_dict = {}
"""not include 8day"""
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            # date = row[1].split(" ")[0][-1]
            date = row[1].split(" ")[0][8:10]
            time = row[1].split(" ")[1].split(":")[0]
            minute = row[1].split(" ")[1].split(":")[1]
            newtime="0"
            if int(time)==12:
                if int(minute)<=30:
                    newtime="12-0"
                else:
                    newtime="12-1"
            if int(time)==13:
                if int(minute)<=30:
                    newtime="13-0"
                else:
                    newtime="13-1"
            if int(time)==14:
                if int(minute)<=30:
                    newtime="14-0"
                else:
                    newtime="14-1"
            key = wifi_name_dict[int(file_name.split(".")[0])]+":"+date+"-"+newtime
            data = float(row[0])
            if newtime=="12-0" or newtime=="12-1" or newtime=="13-0" or newtime=="13-1"\
                    or newtime=="14-0" or newtime=="14-1":
                if key in passengers_count_dict:
                    passengers_count_dict[key] += data
                    time_count_dict[key] += 1
                else:
                    passengers_count_dict[key] = data
                    time_count_dict[key] = 1
                print time_count_dict[key]
    print "writting..."

# # #
# time_stamp_dict=[]
# # time_stamp_sublist = []
# for key in passengers_count_dict:
#     time_stamp_sublist=[float(passengers_count_dict[key])/time_count_dict[key],key.split(":")[0],key.split(":")[1]]
#     time_stamp_dict.append(time_stamp_sublist)
#     # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
# f = open("../gbdt_feat/hlaf_hour_sum.csv", "wb")
# write = csv.writer(f)
# write.writerow(["passengerCount", "wifiap","time"])
# write.writerows(time_stamp_dict)
# f.close()
#
time_stamp_dict={}
for key in passengers_count_dict:
    time_stamp_sublist=float(passengers_count_dict[key])/time_count_dict[key]
    time_stamp_dict[key]=time_stamp_sublist
    # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
f = open("../half_hour_sum_ori.pkl",'wb')
cPickle.dump(time_stamp_dict,f,-1)
f.close()