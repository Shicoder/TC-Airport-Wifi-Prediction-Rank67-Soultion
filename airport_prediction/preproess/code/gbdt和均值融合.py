__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
"""
gbdt_junzhi:97393
gbdt_10:    212987
10_junzhi:  157557
"""
wifi_api_files = file('../test/gbdt_result.csv', 'rb')
# wifi_api_files = file('../test/reslut10_4.csv', 'rb')
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

wifi_api_files = file('../test/airport_gz_passenger_predict_qianhou1_10-14.csv', 'rb')
# wifi_api_files = file('../test/result10_14.csv', 'rb')
# wifi_api_files = file('../test/gbdt_result.csv', 'rb')
rows = csv.reader(wifi_api_files)
rows.next()
print "splitting...."
one_rows1=[]
for row in rows:
    one_row = [float(row[0]),row[1],row[2]]
    one_rows1.append(one_row)
sum1=0
count=0
f = open("../test/gbdt_junzhi_qiuhe_0.7.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])


for i in range(count_row):
    sum=(one_rows[i][0]-one_rows1[i][0])**2
    data=0.7*one_rows[i][0]+0.3*one_rows1[i][0]
    write.writerow([data,one_rows1[i][1],one_rows1[i][2]])
    if sum<1:
        count+=1
    sum1=sum1+sum
print sum1
print "count:",count
f.close()
# import pandas as pd
# df = pd.read_csv('../test/reslut10_4.csv',index_col="WIFIAPTag")
# print df.describe()
