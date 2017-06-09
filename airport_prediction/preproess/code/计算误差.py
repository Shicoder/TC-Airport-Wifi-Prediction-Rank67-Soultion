__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os

direction2 = "../merge_10/"
file_list2 = os.listdir(direction2)
direction = "../di3tian_qianhoujunzhi/"
file_list = os.listdir(direction)
j=0
sum=0
for file_name in file_list:
    time_dict = {}
    time_count_dict = {}

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()

    for file_name2 in file_list2:
        if file_name2.split(".")[0]==file_name.split(".")[0]:

            file_path2 = direction2+file_name2
            rows2 = csv.reader(open(file_path2,'rb'))
            rows2.next()
            for row in rows:
                date ='2016-09-13'
                time_stamp = row[1]
                date_time=date+" "+time_stamp
                for row2 in rows2:
                    if row2[1]==date_time:
                        j+=1
                        count=(float(row[0])-float(row2[0]))**2
                        print count,j
                        sum+=count
print sum
