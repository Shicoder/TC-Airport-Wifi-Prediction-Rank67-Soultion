
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
hour1_mean_dict=cPickle.load(open("../qianhou1hour_mean.pkl","rb"))
simple_day_q2hour=cPickle.load(open("../simple_day_1-2_hour_mean.pkl","rb"))
t250_hour_dict=cPickle.load(open("../2-50_mean.pkl","rb"))
half_hour_dict=cPickle.load(open("../half_hour_sum.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
features=[]
lables=[]
print "generting feat..."
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            date = row[1].split(" ")[0][8:10]
            time = row[1].split(" ")[1].split(":")[0]
            minute = row[1].split(" ")[1].split(":")[1][0]
            if int(time) >= 15 and int(time) <=17 and int(date)>=17 and int(date)<=24:
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
                three_hour_list=[three_hour_dict[simple_hour_name_pre+"6"],three_hour_dict[simple_hour_name_pre+"9"],three_hour_dict[simple_hour_name_pre+"12"]]
                ##############################
                hour1_max=max(simple_hour_list)
                hour1_min=min(simple_hour_list)
                hour3_max=max(three_hour_list)
                hour3_min=min(three_hour_list)
                #####################################time_series###################
                time_series=6*(int(time)%15)+int(minute)+1
                #########################################
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
                ##########################################
                key=wifi_name_dict[int(file_name.split(".")[0])]+"-"+str(row[1].split(" ")[1])
                mean=hour1_mean_dict[key]
                s2_key = simple_hour_name_pre+"13"
                simple_q2=simple_day_q2hour[s2_key]
                half_hour = half_hour_dict[simple_hour_name_pre+"14-1"]
                t250 = t250_hour_dict[wifi_name_dict[int(file_name.split(".")[0])]+":"+date]
                ###################    feature   ################
                feature=[area,int(file_name.split(".")[0]),time_series,simple_hour_list[0],simple_hour_list[1],simple_hour_list[2],
                        simple_hour_list[3],simple_hour_list[4],simple_hour_list[5],
                        simple_hour_list[6],simple_hour_list[7],simple_hour_list[8],
                        three_hour_list[0],three_hour_list[1],three_hour_list[2],
                        hou_mean_6_14,
                        hour1_max,hour1_min,hour3_max,hour3_min,
                        simple_q2,
                        half_hour,
                        t250
                         ]
                lable=int(float(row[0]))
                #########################################################
                features.append(feature)
                lables.append(lable)
# feat=np.array(features)
# print len(features)
# f=open("../gbdt_feat/gbdt2_2_feat.csv","wb")
# write = csv.writer(f)
# write.writerows(feat)
# f.close()


print "start train"
import numpy as np
feat=np.array(features)
la=np.array(lables)
from sklearn.ensemble import GradientBoostingClassifier
clf2=GradientBoostingClassifier(n_estimators=1000,learning_rate=0.1,max_depth=20,max_features=10)
# clf2=GradientBoostingClassifier()
# clf2.fit(x_train,y_train)
print "start fitting"
clf2.fit(feat, la)
print "saving model"
# from sklearn.externals import joblib
# joblib.dump(clf2, '../gbdt_feat/model/gbdt.model')
# jbdt = joblib.load('../gbdt_feat/model/gbdt.model')
# for m in range(len(model.feature_importances_)):
#     if model.feature_importances_[m]>0.05:
#         print "feature_importance",m,model.feature_importances_[m]
print "loading test data"
test = np.loadtxt(open("../gbdt_feat/gbdt2_3_class_feat_online.csv","rb"),delimiter=",",skiprows=0)
import numpy as np
print "predicting"
pre=clf2.predict(test)

f = open("../submit/gbdt2_3_result_classifer_online.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
for i in range(len(pre)):
    pre_date="2016-09-25-"
    wifiname=wifi_name_dict[int(test[i][1])]
    slice10h=15+int(test[i][2]-1)/6
    slice10m=int((test[i][2]-1)%6)
    pre_data=pre_date+str(slice10h)+"-"+str(slice10m)
    write.writerow([str(pre[i]),wifiname,pre_data])
f.close()
for i in range(len(clf2.feature_importances_)):
    print clf2.feature_importances_[i]
