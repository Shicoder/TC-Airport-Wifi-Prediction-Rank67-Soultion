
#-*-coding:utf-8-*-
import csv
import pandas as pd
import os
import cPickle
"""Ԥ�����㵽���㣬wifi�㣬ʱ���任���У����������ֵ���ߵ��ֵ���˵��ֵ���ŵ��ֵ��
ʮ���ֵ��11���ֵ��12���ֵ��1���ֵ��2���ֵ��
6-8��ֵ��9-11��ֵ��12-2��ֵ��ǰ6-14���ֵ��6-8��9-11��9-11��12-2��6-8��12-2��1���ֵ��1��Сֵ��3���3��С��Y�У��˿���"""
passengers_count_dict={}
time_count_dict = {}
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
simple_hour_dict=cPickle.load(open("../simple_hour_sum.pkl","rb"))
three_hour_dict=cPickle.load(open("../3_hour_sum.pkl","rb"))
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
            date = row[1].split(" ")[0][-1]#ȡ��1��2��3
            time = row[1].split(" ")[1].split(":")[0]#ȡ��Сʱ
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
                features.append(feature)
                lables.append(lable)
print "start train"
import numpy as np
feat=np.array(features)
la=np.array(lables)
from sklearn.ensemble import GradientBoostingClassifier
clf2=GradientBoostingClassifier(loss="exponential",n_estimators=1000,learning_rate=0.1,max_depth=20,max_features=10)
# clf2=GradientBoostingClassifier()
# clf2.fit(x_train,y_train)
print "start fitting"
clf2.fit(feat, la)
from sklearn.externals import joblib
joblib.dump(clf2, '../gbdt_feat/model/lr.model')
lr = joblib.load('../gbdt_feat/model/lr.model')
# for m in range(len(model.feature_importances_)):
#     if model.feature_importances_[m]>0.05:
#         print "feature_importance",m,model.feature_importances_[m]
test = np.loadtxt(open("../gbdt_feat/SPSS_feature_pro.csv","rb"),delimiter=",",skiprows=0)
import numpy as np
pre=clf2.predict(test)

f = open("../submit/gbdt_result.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
for i in range(len(pre)):
    pre_date="2016-09-14-"
    wifiname=wifi_name_dict[int(test[i][0])]
    slice10h=15+int(test[i][1]-1)/6
    slice10m=int((test[i][1]-1)%6)
    pre_data=pre_date+str(slice10h)+"-"+str(slice10m)
    write.writerow([str(pre[i]),wifiname,pre_data])
f.close()
for i in range(22):
    print clf2.feature_importances_[i]
