__author__ = 'shi'
import csv
import time,datetime
import os
f = open("D:/fligh/wifiylres2.csv");
rows = csv.reader(f)
rows.next()
flighall=[]
for row in rows:
    """string to data"""
    date = datetime.datetime.strptime(row[-1], '%Y-%m-%d-%H-%M')
    day = date.weekday()
    if day==5 or day==6:
        isweeken=1
    else:
        isweeken=0
        """" change data to minte"""
    row[-1]=int(int(row[-1].split("-")[3])*60+int(row[-1].split("-")[4]))
    flighp=row[0:1]
    flighp.append(row[-1])
    flighp.append(day)
    flighp.append(isweeken)
    flighall.append(flighp)

flighall
