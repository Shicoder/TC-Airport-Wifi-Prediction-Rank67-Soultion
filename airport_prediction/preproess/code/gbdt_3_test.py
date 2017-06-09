
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
direction = "../stddayu1/"
file_list = os.listdir(direction)
train_features=[]
lables=[]
print "generting feat..."
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            date = row[1].split(" ")[0][-1]
            time = row[1].split(" ")[1].split(":")[0]
            minute = row[1].split(" ")[1].split(":")[1][0]
            if int(time) >= 15 and int(time) <=17 and int(date)>=1 and int(date)<=3:
                wifi_name=wifi_name_dict[int(file_name.split(".")[0])]
                simple_hour_name_pre =wifi_name+":"+date+"-"
                #####################
                ########################
                simple_hour_list=[
                        simple_hour_dict[simple_hour_name_pre+"12"],simple_hour_dict[simple_hour_name_pre+"13"],simple_hour_dict[simple_hour_name_pre+"14"]]
                #############################
                three_hours=three_hour_dict[simple_hour_name_pre+"12"]
                two_hours=simple_day_hour1_2_mean[simple_hour_name_pre+"13"]
                #####################################time_series###################
                time_series=6*(int(time)%15)+int(minute)+1
                ###################    feature   ################
                feature=[int(file_name.split(".")[0]),time_series,simple_hour_list[0],simple_hour_list[1],simple_hour_list[2],
                        two_hours,
                        three_hours]
                lable=row[0]
                #########################################################
                train_features.append(feature)
                lables.append(lable)
print "start train"
import numpy as np
feat=np.array(train_features)
la=np.array(lables)
feat=np.asarray(feat, dtype=np.float64)
la=np.asarray(la, dtype=np.float64)
# from sklearn.ensemble import GradientBoostingRegressor
# from sklearn import cross_validation
# # from sklearn.grid_search import GridSearchCV
# # from pprint import pprint
# clf=GradientBoostingRegressor(n_estimators=1000,learning_rate=0.1,max_depth=20)
# # X_train, X_test, y_train, y_test = cross_validation.train_test_split(feat,la, test_size=0.3, random_state=0)
# clf.fit(feat,la)
# parameters = {'loss':['ls','lad','huber','quantile'],'n_estimators': [500, 1500]}
# grid_search = GridSearchCV(estimator=clf,param_grid=parameters, cv=5, scoring='accuracy')
# print("parameters:")
# pprint(parameters)
# grid_search.fit(feat,la)
# print("Best score: %0.3f" % grid_search.best_score_)
# print("Best parameters set:")
# best_parameters=grid_search.best_estimator_.get_params()
# for param_name in sorted(parameters.keys()):
#     print("\t%s: %r" % (param_name, best_parameters[param_name]))
# clf2=GradientBoostingClassifier()
# clf2.fit(x_train,y_train)
print "first fitting end!"
print "saving model"
from sklearn.externals import joblib
# joblib.dump(clf, '../gbdt_feat/model/gbdt_xg1.model')
clf= joblib.load('../gbdt_feat/model/gbdt_xg1.model')
for m in range(len(clf.feature_importances_)):
       print "feature_importance1",m,clf.feature_importances_[m]
####################################################################################
# print "loading test data"
# test = np.loadtxt(open("../gbdt_feat/SPSS_feature_pro.csv","rb"),delimiter=",",skiprows=0)
# import numpy as np
# print "predicting"
# pre=clf2.predict(test)
#######################################################################################################
direction = "../stddayu1/"
file_list = os.listdir(direction)
features=[]
print "generting feat..."
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
    simple_hour_list=[
            simple_hour_dict[simple_hour_name_pre+"12"],simple_hour_dict[simple_hour_name_pre+"13"],simple_hour_dict[simple_hour_name_pre+"14"]]
    #############################
    three_hours=three_hour_dict[simple_hour_name_pre+"12"]
    two_hours=simple_day_hour1_2_mean[simple_hour_name_pre+"13"]
    #####################################time_series###################
    ###################    feature   ################
    for i in range(18):
        feature=[int(file_name.split(".")[0]),i+1,simple_hour_list[0],simple_hour_list[1],simple_hour_list[2],
                two_hours,
                three_hours]
    #########################################################
        features.append(feature)

##########################################################################################################
print "predicting"
feat_T=np.array(features)
feat_T=np.asarray(feat_T, dtype=np.float64)
pre=clf.predict(feat_T)
####################################################################################################
f = open("../submit/two_gbdt_result_3.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
for i in range(len(pre)):
    pre_date="2016-09-14-"
    wifiname=wifi_name_dict[int(features[i][0])]
    slice10h=15+int(features[i][1]-1)/6
    slice10m=int((features[i][1]-1)%6)
    pre_data=pre_date+str(slice10h)+"-"+str(slice10m)
    write.writerow([pre[i],wifiname,pre_data])
######################################################################
################################################################
direction = "../new_mean_result/"
file_list = os.listdir(direction)
result_list = []
for file_name in file_list:
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
        # one_result = row[0],wifi_name_dict[file_name]
        pre_date="2016-09-14-"
        time_stamp1 = row[1].split(":")[0]
        time_stamp2 = row[1].split(":")[1][0:1]
        gang='-'
        pre_date+=time_stamp1
        pre_date+=gang
        pre_date+=time_stamp2
        one_result = [row[0],wifi_name_dict[int(file_name.split(".")[0])],pre_date]
        result_list.append(one_result)
write.writerows(result_list)
f.close()

