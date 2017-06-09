__author__ = 'shi'

# import csv
# f_name_dict={}
#
# wifi_api_files = file('../ori_data/airport_gz_flights_chusai_1stround_s.csv', 'rb')
# rows = csv.reader(wifi_api_files)
# rows.next()
# print "splitting...."
# for row in rows:
#     f_name=row[0]
#     date = row[2]
#     if f_name in f_name_dict:
#         if date not in f_name_dict[f_name]:
#             f_name_dict[f_name].append(date)
#     else:
#         f_name_dict[f_name]=[date]
# wifi_api_files.close()
# #############################################################################
# import datetime
# wifi_api_files = file('../ori_data/airport_gz_security_check_chusai_1stround.csv', 'rb')
# rows = csv.reader(wifi_api_files)
# rows.next()
# print "splitting...."
# one_rows=[]
# for row in rows:
#     one_row = [float(row[0])*0.95,row[1],row[2]]
#     one_rows.append(one_row)
# date = datetime.datetime.strptime(row[-1], '%Y-%m-%d-%H-%M')
# starttime = datetime.datetime.now()
# #long running
# endtime = datetime.datetime.now()
# print (endtime - starttime).seconds
from sklearn.externals import joblib
import cPickle
print "loading model"
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
clf2 = joblib.load('../gbdt_feat/model/rf.model')
# for m in range(len(model.feature_importances_)):
#     if model.feature_importances_[m]>0.05:
#         print "feature_importance",m,model.feature_importances_[m]
print "loading test data"
test = np.loadtxt(open("../gbdt_feat/SPSS_feature_pro.csv","rb"),delimiter=",",skiprows=0)
import numpy as np
print "predicting"
pre=clf2.predict(test)
import csv
f = open("../submit/rf_result.csv", "wb")
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