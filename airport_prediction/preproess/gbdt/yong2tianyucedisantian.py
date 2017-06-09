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
direction = "../merge_10/"
file_list = os.listdir(direction)
features1_2=[]
features3=[]
lables1_2=[]
lables3=[]
print "generting feat..."
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            date = row[1].split(" ")[0][-1]#???1??2??3
            time = row[1].split(" ")[1].split(":")[0]#???��?
            minute = row[1].split(" ")[1].split(":")[1][0]
            if int(time) >= 15 and int(time) <=17 and int(date)>=1 and int(date)<=3:
                wifi_name=wifi_name_dict[int(file_name.split(".")[0])]
                simple_hour_name_pre =wifi_name+":"+date+"-"
                #####################
                hou_mean_6_14=(float(simple_hour_dict[simple_hour_name_pre+"06"])+float(simple_hour_dict[simple_hour_name_pre+"07"])+float(simple_hour_dict[simple_hour_name_pre+"08"])+\
                    float(simple_hour_dict[simple_hour_name_pre+"09"])+float(simple_hour_dict[simple_hour_name_pre+"10"])+float(simple_hour_dict[simple_hour_name_pre+"11"])+\
                    float(simple_hour_dict[simple_hour_name_pre+"12"])+float(simple_hour_dict[simple_hour_name_pre+"13"])+float(simple_hour_dict[simple_hour_name_pre+"14"]))/9.0
                #####################
                compute1 = 1 if three_hour_dict[simple_hour_name_pre+"9"]-three_hour_dict[simple_hour_name_pre+"6"]>0 else -1
                compute2 = 1 if three_hour_dict[simple_hour_name_pre+"12"]-three_hour_dict[simple_hour_name_pre+"9"]>0 else -1
                compute3 = 1 if three_hour_dict[simple_hour_name_pre+"12"]-three_hour_dict[simple_hour_name_pre+"6"]>0 else -1
                ########################
                simple_hour_list=[simple_hour_dict[simple_hour_name_pre+"06"],simple_hour_dict[simple_hour_name_pre+"07"],simple_hour_dict[simple_hour_name_pre+"08"],
                        simple_hour_dict[simple_hour_name_pre+"09"],simple_hour_dict[simple_hour_name_pre+"10"],simple_hour_dict[simple_hour_name_pre+"11"],
                        simple_hour_dict[simple_hour_name_pre+"12"],simple_hour_dict[simple_hour_name_pre+"13"],simple_hour_dict[simple_hour_name_pre+"14"]]
                #############################
                three_hour_list=[three_hour_dict[simple_hour_name_pre+"6"],three_hour_dict[simple_hour_name_pre+"9"],three_hour_dict[simple_hour_name_pre+"12"]]
                ##############################
                hour1_max=max(simple_hour_list)
                hour1_min=min(simple_hour_list)
                hour3_max=max(three_hour_list)
                hour3_min=min(three_hour_list)
                #####################################time_series###################
                time_series=6*(int(time)%15)+int(minute)+1
                ###################    feature   ################
                feature=[int(file_name.split(".")[0]),time_series,simple_hour_list[0],simple_hour_list[1],simple_hour_list[2],
                        simple_hour_list[3],simple_hour_list[4],simple_hour_list[5],
                        simple_hour_list[6],simple_hour_list[7],simple_hour_list[8],
                        three_hour_list[0],three_hour_list[1],three_hour_list[2],
                        hou_mean_6_14,
                        compute1,compute2,compute3,
                        hour1_max,hour1_min,hour3_max,hour3_min]
                lable=row[0]
                #########################################################
                if int(date)==3:
                    features3.append(feature)
                    lables3.append(lable)
                else:
                    features1_2.append(feature)
                    lables1_2.append(lable)
print "start train"
import numpy as np
feat=np.array(features1_2)
la=np.array(lables1_2)
from sklearn.ensemble import GradientBoostingClassifier
clf2=GradientBoostingClassifier()
# clf2.fit(x_train,y_train)
print "start fitting"
clf2.fit(feat, la)
import cPickle
cPickle.dump("../gbdt_feat/model_1_2.pkl",clf2)