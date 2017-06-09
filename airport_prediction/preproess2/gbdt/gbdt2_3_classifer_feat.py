
#-*-coding:utf-8-*-
import csv
import pandas as pd
import os
import cPickle
passengers_count_dict={}
time_count_dict = {}
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
simple_hour_dict=cPickle.load(open("../simple_hour_sum.pkl","rb"))
three_hour_dict=cPickle.load(open("../3_hour_sum.pkl","rb"))
hour1_mean_dict=cPickle.load(open("../qianhou1hour_mean.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
features=[]
print "generting feat..."
for file_name in file_list:
    file_path = direction+file_name
    wifi_name=wifi_name_dict[int(file_name.split(".")[0])]
    # if int(file_name.split(".")[0])==348 or int(file_name.split(".")[0])==383 or int(file_name.split(".")[0])==520 or\
    #                 int(file_name.split(".")[0])==53 or int(file_name.split(".")[0])==736:
    #     simple_hour_name_pre =wifi_name+":"+str(3)+"-"
    # else:
    simple_hour_name_pre =wifi_name+":"+str(25)+"-"
    print "file",int(file_name.split(".")[0])
    #####################
    hou_mean_6_14=(float(simple_hour_dict[simple_hour_name_pre+"6"])+float(simple_hour_dict[simple_hour_name_pre+"7"])+float(simple_hour_dict[simple_hour_name_pre+"8"])+\
    float(simple_hour_dict[simple_hour_name_pre+"9"])+float(simple_hour_dict[simple_hour_name_pre+"10"])+float(simple_hour_dict[simple_hour_name_pre+"11"])+\
    float(simple_hour_dict[simple_hour_name_pre+"12"])+float(simple_hour_dict[simple_hour_name_pre+"13"])+float(simple_hour_dict[simple_hour_name_pre+"14"]))/9.0
    #####################
    ########################
    simple_hour_list=[simple_hour_dict[simple_hour_name_pre+"6"],simple_hour_dict[simple_hour_name_pre+"7"],simple_hour_dict[simple_hour_name_pre+"8"],
            simple_hour_dict[simple_hour_name_pre+"9"],simple_hour_dict[simple_hour_name_pre+"10"],simple_hour_dict[simple_hour_name_pre+"11"],
            simple_hour_dict[simple_hour_name_pre+"12"],simple_hour_dict[simple_hour_name_pre+"13"],simple_hour_dict[simple_hour_name_pre+"14"]]
    #############################
    three_hour_list=[three_hour_dict[simple_hour_name_pre+"6"],three_hour_dict[simple_hour_name_pre+"9"],three_hour_dict[simple_hour_name_pre+"12"]]
    ##############################
    hour1_max=max(simple_hour_list)
    hour1_min=min(simple_hour_list)
    hour3_max=max(three_hour_list)
    hour3_min=min(three_hour_list)
    #####################################time_series###################
    ###################    feature   ################
    for i in range(18):
        time=15+(i/6)
        minte=i%6
        time=str(time)+":"+str(minte)+"0"
        key=wifi_name_dict[int(file_name.split(".")[0])]+"-"+str(time)
        mean=hour1_mean_dict[key]
        feature=[int(file_name.split(".")[0]),i+1,simple_hour_list[0],simple_hour_list[1],simple_hour_list[2],
                simple_hour_list[3],simple_hour_list[4],simple_hour_list[5],
                simple_hour_list[6],simple_hour_list[7],simple_hour_list[8],
                three_hour_list[0],three_hour_list[1],three_hour_list[2],
                hou_mean_6_14,
                hour1_max,hour1_min,hour3_max,hour3_min
                 ]
    #########################################################
        features.append(feature)
import numpy as np
feat=np.array(features)
print len(features)
f=open("../gbdt_feat/gbdt2_3_class_feat.csv","wb")
write = csv.writer(f)
write.writerows(feat)
f.close()