
#-*-coding:utf-8-*-
import csv
import pandas as pd
import os
import cPickle
import numpy as np

passengers_count_dict={}
time_count_dict = {}
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
simple_hour_dict=cPickle.load(open("../simple_hour_sum.pkl","rb"))
three_hour_dict=cPickle.load(open("../3_hour_sum.pkl","rb"))
simple_day_hour1_2_mean=cPickle.load(open("../simple_day_1-2_hour_mean.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
train_features=[]
lables=[]
print "generting feat..."

num_files=0
filesun_dict={}
for filen in file_list:
    filesun_dict[filen.split(".")[0]]=num_files
    num_files+=1

for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            date = row[1].split(" ")[0][-1]
            time = row[1].split(" ")[1].split(":")[0]
            minute = row[1].split(" ")[1].split(":")[1][0]
            # if int(time) >= 15 and int(time) <=17 and int(date)>=1 and int(date)<=3:
            if int(time) >= 15 and int(time) <=17 and int(date)>=1 and int(date)<=3:
                wifi_name=wifi_name_dict[int(file_name.split(".")[0])]
                simple_hour_name_pre =wifi_name+":"+date+"-"
                ###################
                ########################
                simple_hour=simple_hour_dict[simple_hour_name_pre+"14"]
                #############################
                two_hours=simple_day_hour1_2_mean[simple_hour_name_pre+"13"]
                #####################################time_series###################
                time_series=6*(int(time)%15)+int(minute)
                time_list=[0]*18
                time_list[time_series]=1
                ##############################
                file_sum = [0]*num_files
                file_sum[filesun_dict[file_name.split(".")[0]]]=1
                #################################
                feature=[]
                lable=[]
                feature.extend(time_list)
                feature.extend(file_sum)
                feature.append(simple_hour)
                feature.append(two_hours)
                lable.append(row[0])
                ###################    feature   ################

                #########################################################
                train_features.append(feature)
                lables.append(lable)
train_feat=np.array(train_features)
train_la=np.array(lables)

f = open("../gbdt_feat/xishujuzheng_feat.csv", "wb")
write = csv.writer(f)
write.writerows(train_feat)
f.close()
f = open("../gbdt_feat/xishujuzheng_lable.csv", "wb")
write = csv.writer(f)
write.writerows(train_la)
f.close()
################################################
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
feat=np.array(features)
#######################################################
print "loading xgboost"
import xgboost_model
pre=xgboost_model.xgboost_pred(train_feat,train_la,feat)

######################svm#########
f = open("../submit/xgboost_xisu_result.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
direction = "../merge_10/"
file_list = os.listdir(direction)
for filen in file_list:
    pre_date="2016-09-14-"
    wifiname=wifi_name_dict[int(filen.split(".")[0])]
    for i in range(18):
        slice10h=15+(i-1)/6
        slice10m=int((i-1)%6)
        pre_data=pre_date+str(slice10h)+"-"+str(slice10m)
        write.writerow([pre[i],wifiname,pre_data])
f.close()
#######################################################
f = open("../submit/xgb_2.csv", "wb")
write = csv.writer(f)
write.writerows(pre)
f.close()