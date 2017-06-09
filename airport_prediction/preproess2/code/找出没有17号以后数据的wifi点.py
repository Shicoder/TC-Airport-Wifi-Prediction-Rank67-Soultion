import csv
import pandas as pd
import os
import cPickle
"""
160.csv
292.csv
347.csv
385.csv
471.csv
499.csv
596.csv
84.csv"""
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))

direction = "../merge_10/"
file_list = os.listdir(direction)
result_list = []
for file_name in file_list:
    flag=0
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
        date = row[1].split(" ")[0][8:10]
        if int(date)>17:
            flag=1
    if flag==0:
        print file_name
