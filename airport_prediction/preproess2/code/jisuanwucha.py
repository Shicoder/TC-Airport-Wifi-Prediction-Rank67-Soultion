__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
"""
gbdt_junzhi:97393
gbdt_10:    212987
10_junzhi:  157557
GBDT_GBDT-3-2:109515.001702
GBDT3-2(gbdt_3.py)_JUNZHI:184270.774237
gbdt_spss(gbdt_2.py)_junzhi:101227.075166
gbdt_spps_10:101227.075166
gbdt_spss_gbdt-3-2:94452.576469
gdbt-spss_gbst:30933.9766557
"""
# wifi_api_files = file('../test/gbdt3_1_result_withq2_3_half_nomean.csv', 'rb')
# wifi_api_files = file('../test/two_gbdt_result_4_m.csv', 'rb')
# wifi_api_files = file('../test/two_gbdt_result_3_2.csv', 'rb')
# wifi_api_files = file('../test/reslut10_4.csv', 'rb')
wifi_api_files=file('../test/offline_groundtruth_18.csv')
# wifi_api_files = file('../test/gbdtpjf_feat_result.csv', 'rb')
# wifi_api_files = file('../test/gbdt_junzhi_qiuhe_0.5.csv', 'rb')
# wifi_api_files = file('../test/airport_gz_passenger_predict_qianhou1_10-14.csv', 'rb')
rows = csv.reader(wifi_api_files)
rows.next()
print "splitting...."
one_rows=[]
count_row=0
for row in rows:
    one_row = [float(row[0]),row[1],row[2]]
    one_rows.append(one_row)
    count_row+=1

print "writting...",count_row
# wifi_api_files = file('../test/gbdt2_4_result_2_no_mean_no_simple1_no3_1.csv', 'rb')
# wifi_api_files = file('../test/airport_gz_passenger_predict_offline_win5_test.csv', 'rb')
wifi_api_files = file('predict_xgboost_best_muce.csv', 'rb')
# wifi_api_files = file('../test/predict_xgboostfph.csv', 'rb')
# wifi_api_files = file('../test/airport_gz_passenger_predict_win_5day(19-24).csv', 'rb')
# wifi_api_files = file('../test/gbdt4ronghe.csv', 'rb')
rows = csv.reader(wifi_api_files)
rows.next()
print "splitting...."
one_rows1=[]
for row in rows:
    one_row = [float(row[0]),row[1],row[2]]
    one_rows1.append(one_row)
sum1=0
count=0
f = open("../test/bijiao.csv", "wb")
write = csv.writer(f)
write.writerow(["passengerCount", "wifi","timeStamp"])

new_dict=[]
import cPickle
def get_num(get_value):
    key_list = []
    value_list = []
    wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
    for key,value in wifi_name_dict.items():
        key_list.append(key)
        value_list.append(value)

    # get_value = "E2-3B<E2-3-16>"
    if get_value in value_list:
        get_value_index = value_list.index(get_value)
        print "key:" ,key_list[get_value_index]
        return key_list[get_value_index]
for i in range(count_row):
    sum=(one_rows[i][0]-one_rows1[i][0])**2
    write.writerow([one_rows[i][0]-one_rows1[i][0],one_rows1[i][1],one_rows1[i][2]])
    if sum<1:
        count+=1
        if get_num(one_rows1[i][1]) not in new_dict:
            new_dict.append(get_num(one_rows1[i][1]))
    sum1=sum1+sum
print len(new_dict)
print new_dict
print sum1
print "count:",count
f.close()
# import pandas as pd
# df = pd.read_csv('../test/reslut10_4.csv',index_col="WIFIAPTag")
# print df.describe()
