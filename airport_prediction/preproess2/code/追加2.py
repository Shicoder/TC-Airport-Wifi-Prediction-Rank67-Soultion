__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os

direction = "../merge_10_add_predict/"
file_list = os.listdir(direction)

for file_name in file_list:
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    list1= []
    for row in rows:
        data = row[1].split(" ")[0][8:10]
        time = row[1].split(" ")[1].split(":")[0]
        if (int(data)==25) and int(time)>=15 and int(time)<=18:
            list1.append([row[0],row[1]])
    f=open("../merge_10_add_predict2/"+file_name,"wb")
    write = csv.writer(f)
    write.writerow(["passengerCount","timeStamp"])
    write.writerows(list1)
    f.close()