
#-*-coding:utf-8-*-
import csv
import pandas as pd
import os
import cPickle
import numpy as np
passengers_count_dict={}
time_count_dict = {}
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
simple_hour_dict=cPickle.load(open("../simple_hour_sum_ori.pkl","rb"))
three_hour_dict=cPickle.load(open("../3_hour_sum_ori.pkl","rb"))
four_hour_dict=cPickle.load(open("../4_hour_sum_ori.pkl","rb"))
hour1_mean_dict=cPickle.load(open("../qianhou5hour_mean_ori.pkl","rb"))
simple_day_q2hour=cPickle.load(open("../simple_day_1-2_hour_mean_ori.pkl","rb"))
sd_win5_dict = cPickle.load(open("../simple_win_5_mean_ori.pkl","rb"))
half_hour_dict=cPickle.load(open("../half_hour_sum_ori.pkl","rb"))
t250_hour_dict=cPickle.load(open("../2-50_mean_ori.pkl","rb"))
t240_hour_dict=cPickle.load(open("../2-40_mean_ori.pkl","rb"))
t230_hour_dict=cPickle.load(open("../2-30_mean_ori.pkl","rb"))
two_hour_dict=cPickle.load(open("../2_hour_sum_ori.pkl","rb"))
# meidian=cPickle.load(open("../simple_win_9_meidian_ori.pkl","rb"))
# pjf_feat_target=cPickle.load(open("../pjf_feat_predict(1).pkl","rb"))
pjf_feat_train=cPickle.load(open("../pjf_feat_train_quyurenshu.pkl","rb"))
meidian_win5 = cPickle.load(open("../all_win_5_meidian.pkl","rb"))

direction = "../merge_10/"
file_list = os.listdir(direction)
features=[]
lables=[]
f=open("../gbdt_feat/xgboost_train_lable.csv","wb")
write = csv.writer(f)
print "generting feat..."
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            date = row[1].split(" ")[0][8:10]
            time = row[1].split(" ")[1].split(":")[0]
            minute = row[1].split(" ")[1].split(":")[1][0]
            if int(time) >= 15 and int(time) <=17 and ((int(date)>=11 and int(date)<=17) or (int(date)>19 and int(date)<=23)):
                wifi_name=wifi_name_dict[int(file_name.split(".")[0])]
                simple_hour_name_pre =wifi_name+":"+date+"-"
                #####################
                hou_mean_6_14=(float(simple_hour_dict[simple_hour_name_pre+"6"])+float(simple_hour_dict[simple_hour_name_pre+"7"])+float(simple_hour_dict[simple_hour_name_pre+"8"])+\
                    float(simple_hour_dict[simple_hour_name_pre+"9"])+float(simple_hour_dict[simple_hour_name_pre+"10"])+float(simple_hour_dict[simple_hour_name_pre+"11"])+\
                    float(simple_hour_dict[simple_hour_name_pre+"12"])+float(simple_hour_dict[simple_hour_name_pre+"13"])+float(simple_hour_dict[simple_hour_name_pre+"14"]))/9.0
                #####################
                compute1 = 1 if three_hour_dict[simple_hour_name_pre+"9"]-three_hour_dict[simple_hour_name_pre+"6"]>0 else -1
                compute2 = 1 if three_hour_dict[simple_hour_name_pre+"12"]-three_hour_dict[simple_hour_name_pre+"9"]>0 else -1
                compute3 = 1 if three_hour_dict[simple_hour_name_pre+"12"]-three_hour_dict[simple_hour_name_pre+"6"]>0 else -1
                ########################
                simple_hour_list=[simple_hour_dict[simple_hour_name_pre+"6"],simple_hour_dict[simple_hour_name_pre+"7"],simple_hour_dict[simple_hour_name_pre+"8"],
                        simple_hour_dict[simple_hour_name_pre+"9"],simple_hour_dict[simple_hour_name_pre+"10"],simple_hour_dict[simple_hour_name_pre+"11"],
                        simple_hour_dict[simple_hour_name_pre+"12"],simple_hour_dict[simple_hour_name_pre+"13"],simple_hour_dict[simple_hour_name_pre+"14"]]
                #############################
                half_hour_list = [half_hour_dict[simple_hour_name_pre+"12-0"],half_hour_dict[simple_hour_name_pre+"12-1"],
                      half_hour_dict[simple_hour_name_pre+"13-0"],half_hour_dict[simple_hour_name_pre+"13-1"],
                      half_hour_dict[simple_hour_name_pre+"14-0"],half_hour_dict[simple_hour_name_pre+"14-1"]]
                four_hour = four_hour_dict[simple_hour_name_pre+"11"]
                three_hour_list=[three_hour_dict[simple_hour_name_pre+"6"],three_hour_dict[simple_hour_name_pre+"9"],three_hour_dict[simple_hour_name_pre+"12"]]
                two_hour_list=[two_hour_dict[simple_hour_name_pre+"9"],two_hour_dict[simple_hour_name_pre+"11"],two_hour_dict[simple_hour_name_pre+"13"]]
                ##############################
                hour1_max=max(simple_hour_list)
                hour1_min=min(simple_hour_list)
                hour3_max=max(three_hour_list)
                hour3_min=min(three_hour_list)
                #####################################time_series###################
                time_series=6*(int(time)%15)+int(minute)+1
                #########################################
                key=wifi_name_dict[int(file_name.split(".")[0])]+"-"+str(row[1].split(" ")[1])
                mean=hour1_mean_dict[key]
                area=0
                if wifi_name[0:2]=='E1'or wifi_name[0:2]=='e1':
                    area = 1
                elif wifi_name[0:2]=='E2'or wifi_name[0:2]=='e2':
                    area = 2
                elif wifi_name[0:2]=='E3'or wifi_name[0:2]=='e3':
                    area = 3
                elif wifi_name[0:2]=='EC'or wifi_name[0:2]=='Ec':
                    area = 4
                elif wifi_name[0:2]=='T1'or wifi_name[0:2]=='t1':
                    area = 5
                elif wifi_name[0:2]=='W1'or wifi_name[0:2]=='w1':
                    area = 6
                elif wifi_name[0:2]=='W2'or wifi_name[0:2]=='w2':
                    area = 7
                elif wifi_name[0:2]=='W3'or wifi_name[0:2]=='w3':
                    area = 8
                elif wifi_name[0:2]=='WC'or wifi_name[0:2]=='wc' or wifi_name[0:2]=='Wc':
                    area = 9
                else:
                    print wifi_name[0:2]
########################################################
                s2_key = wifi_name_dict[int(file_name.split(".")[0])]+":"+date+"-13"
                simple_q2=simple_day_q2hour[s2_key]
                ph_key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+str(date)+"-"+str(time_series)
                print sd_win5_dict["WC-3C<WC-3-13>-20-9"]
                s1 = sd_win5_dict[ph_key]
                # pjf_key=file_name.split(".")[0]+"-"+date+"-"+str(time_series)
                # pif_feat=pjf_feat_train[pjf_key]##
                # meidian_num = meidian[wifi_name_dict[int(file_name.split(".")[0])]+"-"+date+"-"+str(time_series)]
                t230 = t230_hour_dict[wifi_name_dict[int(file_name.split(".")[0])]+":"+date]
                t240 = t240_hour_dict[wifi_name_dict[int(file_name.split(".")[0])]+":"+date]
                t250 = t250_hour_dict[wifi_name_dict[int(file_name.split(".")[0])]+":"+date]
                meidian_key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+str(time_series)
                meidian_mean=meidian_win5[meidian_key]
                ###################    feature   ################
                feature=[area,int(file_name.split(".")[0]),time_series,simple_hour_list[0],simple_hour_list[1],simple_hour_list[2],
                        simple_hour_list[3],simple_hour_list[4],simple_hour_list[5],
                        simple_hour_list[6],simple_hour_list[7],simple_hour_list[8],
                        three_hour_list[0],three_hour_list[1],three_hour_list[2],
                        hou_mean_6_14,
                        hour1_max,hour1_min,hour3_max,hour3_min,
                        mean,
                        two_hour_list[0],
                        two_hour_list[1],
                        simple_q2,
                        half_hour_list[0],half_hour_list[1],half_hour_list[2],
                        half_hour_list[3],half_hour_list[4],half_hour_list[5],
                        t230,
                        t240,
                        t250,
                        four_hour,
                        # meidian_mean
                         ]
                # feature.extend(pif_feat)
                lable=row[0]
                write.writerow([lable])
                #########################################################
                features.append(feature)

f.close()
f=open("../gbdt_feat/xgboost_feat_train.csv","wb")
write = csv.writer(f)
write.writerows(features)
f.close()

