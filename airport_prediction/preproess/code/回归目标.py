
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
simple_day_hour1_2_mean=cPickle.load(open("../simple_day_1-2_hour_mean.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
features=[]
print "generting feat..."
num_files=0
filesun_dict={}
for filen in file_list:
    filesun_dict[filen.split(".")[0]]=num_files
    num_files+=1
for file_name in file_list:
    file_path = direction+file_name
    wifi_name=wifi_name_dict[int(file_name.split(".")[0])]
    if int(file_name.split(".")[0])==348 or int(file_name.split(".")[0])==383 or int(file_name.split(".")[0])==520 or\
                    int(file_name.split(".")[0])==53 or int(file_name.split(".")[0])==736:
        simple_hour_name_pre =wifi_name+":"+str(3)+"-"
    else:
        simple_hour_name_pre =wifi_name+":"+str(4)+"-"
    print "file",int(file_name.split(".")[0])
    #####################
    ########################
    simple_hour=simple_hour_dict[simple_hour_name_pre+"14"]
    #############################
    two_hours=simple_day_hour1_2_mean[simple_hour_name_pre+"13"]
    #####################################time_series###################
    ##############################
    file_sum = [0]*num_files
    file_sum[filesun_dict[file_name.split(".")[0]]]=1
    print "file_feat:",len(file_sum)
    #################################
    for i in range(18):
        time_list=[0]*18
        time_list[i]=1
        feature=[]
        feature.extend(time_list)
        feature.extend(file_sum)
        feature.append(simple_hour)
        feature.append(two_hours)
        print "feature length:",len(feature)
        ###################    feature   ################

            #########################################################
        features.append(feature)

    #####################################time_series###################
    ###################    feature   ################
import numpy as np
feat=np.array(features)
print len(features)
f=open("../gbdt_feat/xishujuzheng_feature_predict.csv","wb")
write = csv.writer(f)
write.writerows(feat)
f.close()