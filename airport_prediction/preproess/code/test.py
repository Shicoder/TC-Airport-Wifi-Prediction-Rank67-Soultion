__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
wifi_ap_dict={}

wifi_api_files = file('../test/reslut10_4.csv', 'rb')
rows = csv.reader(wifi_api_files)
rows.next()
print "splitting...."
one_rows=[]
for row in rows:
    one_row = [float(row[0])*0.95,row[1],row[2]]
    one_rows.append(one_row)

print "writting..."
f=open("../test/airport_gz_passenger_predict.csv","wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
write.writerows(one_rows)
f.close()