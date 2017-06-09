__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import cPickle
wifi_ap_dict={}

wifi_api_files = file('../ori_data/WIFI_AP_Passenger_Records_chusai_1stround.csv', 'rb')
rows = csv.reader(wifi_api_files)
rows.next()
print "splitting...."
wifi_ap_names=[]
for row in rows:
    u1,u2,u3,u4,u5,u6= row[2].split('-')
    gang = '-'
    maohao = ':'
    u1+=gang
    u1+=u2
    u1+=gang
    u1+=u3

    u4+=maohao
    u4+=u5
    u4+=maohao
    u4+=u6
    wifi_name = row[0]
    # wifi_ap_names.append(wifi_name)
    # # kong= ' '
    # row_2_2 = row[2][11:]
    # row_2_2 = row_2_2.replace('-',':')
    row_2 =u1+' '+u4
    # row_2 += kong
    # row_2 += row[2][-7:]

    # new_time = list(row[2])
    # new_time[11] = ' '
    # str_new_time = ''.join(new_time)
    data=[row[1],row_2,row[3]]
    if wifi_name in wifi_ap_dict:
        wifi_ap_dict[wifi_name].append(data)
    else:
        wifi_ap_dict[wifi_name]=[data]
wifi_api_files.close()
i=1

print "writting..."
wifi_name_dict = {}
for wifi_name in wifi_ap_dict:
    wifi_name_dict[i] = wifi_name
    f = open("../data/"+str(i)+".csv", "wb")
    write = csv.writer(f)
    write.writerow(["passengerCount", "timeStamp","MAC"])
    write.writerows(wifi_ap_dict[wifi_name])
    i=i+1
    f.close()
# series_wifi=pd.Series(wifi_ap_dict)
# f=open("../data/wifi_names.csv","wb")
# write = csv.writer(f)
# write.writerows(series_wifi[0])
f = open("../wifi_name_dict.pkl",'wb')
cPickle.dump(wifi_name_dict,f,-1)
f.close()
print len(wifi_ap_names)