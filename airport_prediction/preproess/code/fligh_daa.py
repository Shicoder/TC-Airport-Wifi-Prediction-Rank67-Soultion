#-*-coding:utf-8-*-
import csv
import time,datetime
import os
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# f = open("d:/fligh/yuan/fligh.csv");
# rows = csv.reader(f)
# rows.next()
# flighall=[]
# for row in rows:
#     o = datetime.timedelta(hours=8)
#     if row[-1]!='':
#         if row[-3].find(":") != -1:
#             date1 = datetime.datetime.strptime(row[-3], '%Y/%m/%d %H:%M:%S')
#             date1 = date1 + o
#         else:
#             date1 = datetime.datetime.strptime(row[-3], '%Y/%m/%d')
#             date1 = date1 + o
#         row[-3] = date1.strftime('%Y-%m-%d %H:%M:%S')
#         if row[-2]=='':
#             row[-2]=row[-3]
#         else:
#             if row[-2].find(":") != -1:
#                 date1 = datetime.datetime.strptime(row[-2], '%Y/%m/%d %H:%M:%S')
#                 date1 = date1 + o
#             else:
#                 date1 = datetime.datetime.strptime(row[-2], '%Y/%m/%d')
#                 date1 = date1 + o
#             row[-2] = date1.strftime('%Y-%m-%d %H:%M:%S')
#         if row[-1].find(',') != -1:
#             o2 = datetime.timedelta(hours=1)
#             fligh1 = row[-1].split(",")[0]
#             fligh2 = row[-1].split(",")[1]
#             # time1 = datetime.datetime.strptime(row[-2], '%Y/%m/%d %H:%M:%S')
#             # time2 = datetime.datetime.strptime(row[-3], '%Y/%m/%d %H:%M:%S')
#             flighp=row[0:3]
#             flighp.append(fligh1)
#             flighall.append(flighp)
#             flighp2=row[0:3]
#             flighp2.append(fligh2)
#             flighall.append(flighp2)
#         else:
#             flighall.append(row[0:4])
# flighda = pd.DataFrame(np.array(flighall),columns=['flight_ID','scheduled_flt_time','actual_flt_time','BGATE_ID'])
# flighda.to_csv("d:/fligh/10_17/fligh1.csv",sep=',',index=False)
# datagae = pd.read_csv("D:/fligh/yuan/gz_ga.csv",sep=",",index_col='BGATE_ID')
# datagaesc = pd.read_csv("d:/fligh/10_17/fligh1.csv",sep=",",index_col='BGATE_ID')
# datagaescs = datagaesc.join(datagae)
# datagaescs.to_csv('d:/fligh/10_17/fligh_gzjoin.csv',sep=',')
#
# f = open("d:/fligh/10_17/fligh_gzjoin.csv");
# rows = csv.reader(f)
# rows.next()
# flighall=[]
# for row in rows:
#     fligh=row
#     fligh.append(row[1]+(row[2].split(" ")[0]))
#     flighall.append(fligh)
# flighda = pd.DataFrame(np.array(flighall),columns=['BGATE_ID','flight_ID','scheduled_flt_time','actual_flt_time','BGATE_AREA','flight_ID_time'])
# flighda.to_csv("d:/fligh/10_17/fligh_gzjoin.csv",sep=',',index=False)
#
# f = open("D:/fligh/yuan/secur.csv");
# rows = csv.reader(f)
# rows.next()
# flighall=[]
# for row in rows:
#     fligh=row
#     fligh.append(row[2]+(row[1].split(" ")[0]))
#     flighall.append(fligh)
# flighda = pd.DataFrame(np.array(flighall),columns=['passenger_ID','security_time','flight_ID1','flight_ID_time'])
# flighda.to_csv("d:/fligh/10_17/secur.csv",sep=',',index=False)
#
# seurdaa = pd.read_csv("D:/fligh/10_17/secur.csv",sep=",",index_col='flight_ID_time')
# fligh_gzjoin = pd.read_csv('d:/fligh/10_17/fligh_gzjoin.csv',sep=',',index_col='flight_ID_time')
# fligh_gzjoinse=seurdaa.join(fligh_gzjoin)
# fligh_gzjoinse.to_csv('d:/fligh/10_17/fligh_gzserjoin.csv',sep=',')


# wifi = pd.read_csv('d:/fligh/10_17/wifi.txt',sep=',')
# f = open("d:/fligh/10_17/wifi_avg.txt");
# rows = csv.reader(f)
# rows.next()
# flighall=[]
# for row in rows:
#     fligh=row
#     fligh.append(row[0]+row[1].split('-')[0]+'-'+row[1].split('-')[1]+'-'+row[1].split('-')[2])
#     flighall.append(fligh)
# flighda = pd.DataFrame(np.array(flighall),columns=['wifi','time','p','wifitime'])
# for name ,group in flighda.groupby(flighda['wifitime']):
#     group.to_csv("d:/fligh/10_17/wifi_fenxi/%s.csv"%(name.split('<')[0]+name.split('>')[1]),index=False)

# wifi = pd.read_csv('D:/fligh/10_17/wifi_fenxi/E1-1A-12016-09-11.csv',sep=',')
# plt.plot(wifi['time'].map(lambda x:x.split('-')[3]),wifi['p'])
# plt.show()
# wifi = pd.read_csv('D:/fligh/10_17/wifi_fenxi/E1-1A-12016-09-17.csv',sep=',')
# plt.plot(wifi['time'].map(lambda x:x.split('-')[3]),wifi['p'])
# plt.show()
# wifi = pd.read_csv('D:/fligh/10_17/wifi_fenxi/E1-1A-12016-09-18.csv',sep=',')
# plt.plot(wifi['time'].map(lambda x:x.split('-')[3]),wifi['p'])
# plt.show()
# wifi = pd.read_csv('D:/fligh/10_17/wifi_fenxi/E1-1A-12016-09-24.csv',sep=',')
# plt.plot(wifi['time'].map(lambda x:x.split('-')[3]),wifi['p'])
# plt.show()
# d:/fligh/10_17/fligh_gzserjoin.csv
# plt.plot(wifi['time'].map(lambda x:x.split('-')[3]),wifi['p'])
# plt.show()

# """
# 160.csv
# 292.csv
# 347.csv
# 385.csv
# 471.csv
# 499.csv
# 596.csv
# 84.csv"""
# wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))

#
# import csv
# import time, datetime
# import os
# flighpp={}
# flighp={}
# f = open("d:/fligh/yuan/fligh.csv");
# rows = csv.reader(f)
# rows.next()
# flighpp={}
# flighp={}
# for row in rows:
#     if row[-1]!='':
#         if row[-1].find(',')!=-1:
#             row[1]=(row[1].split(" ")[0]).split("/")[0]+'-0'+(row[1].split(" ")[0]).split("/")[1]+'-'+(row[1].split(" ")[0]).split("/")[2]
#             value = row[0]+row[1]
#             fligh1 = row[-1].split(",")[0]
#             flighpp[fligh1]=value
#             fligh2 = row[-1].split(",")[1]
#             flighp[fligh2]=value
#
# f = open("d:/fligh/10_17/fligh_gzserjoin.csv");
# flighalls=[]
# rows = csv.reader(f)
# rows.next()
# for row in rows:
#     if int(row[0].split('-')[2])>16 :
#         o = datetime.timedelta(hours=0.5)
#         if flighpp.has_key(row[1]):
#             if flighpp[row[4]] == row[0]:
#                 if row[-2] != '':
#                     date1 = datetime.datetime.strptime(row[-2], '%Y-%m-%d %H:%M:%S')
#                     date1 = date1 - o
#                     date2 = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
#                     if date2 > date1:
#                         break;
#                     flighps = row[0:7]
#                     flighps.append(date1.strftime('%Y-%m-%d %H:%M:%S'))
#                     flighps.append(row[-1])
#                     flighalls.append(flighps)
#         elif flighp.has_key(row[4]):
#             if flighp[row[4]] == row[0]:
#                 if row[-2] != '':
#                     date1 = datetime.datetime.strptime(row[-2], '%Y-%m-%d %H:%M:%S')
#                     date1 = date1 - o
#                     date2 = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
#                     if date2 > date1:
#                         date1 = date2;
#                     flighps = row[0:2]
#                     flighps.append(date1.strftime('%Y-%m-%d %H:%M:%S'))
#                     flighps.append(row[3])
#                     flighps.append(row[4])
#                     flighps.append(row[5])
#                     flighps.append(row[6])
#                     flighps.append(row[7])
#                     flighps.append(row[-1])
#                     flighalls.append(flighps)
#         else:
#             if row[-2] != '':
#                 flighps = row
#                 flighalls.append(flighps)
#
# flighda = pd.DataFrame(np.array(flighalls),columns=['flighttimeag', 'passenger_ID', 'security_time', 'flight_ID_2', 'BGATE_ID', 'flight_ID',
#                                 'scheduled_flt_time', 'actual_flt_time', 'BGATE_AREA'])
# flighda.to_csv("d:/fligh/10_17/joinanjianpeonum.csv",index=False)
#
#
#
allimr = []
for i in range(17,25):
   for j in range(15,18):
       for g in range(0,60):
        ime = "2016-09-%d-%d-%d"%(i,j,g)
        allimr.append(ime)

# pd.DataFrame(np.array(allimr), columns=['time']).to_csv('d:/fligh/10_17/time.csv', index=False)
# joinanjianpeonum=pd.read_csv('d:/fligh/10_17/joinanjianpeonum.csv',sep=',')
# for name,group in joinanjianpeonum.groupby('BGATE_AREA'):
#     group.to_csv("d:/fligh/10_17/%s.csv"%name,index=False)

import csv
import time, datetime
import os

for j in range(1, 2):
    for g in range(3, 4):
        numdae = []
        if j == 0:
            srr = 'E%d' % g;
        if j == 1:
            srr = 'W%d' % g
        for i in allimr:
            date1 = datetime.datetime.strptime(i, '%Y-%m-%d-%H-%M')
            o = datetime.timedelta(hours=0.2)
            f = open("../pjf_data/%s.csv" % srr);
            rows = csv.reader(f)
            rows.next()
            num = 0
            for row in rows:
                numda = []
                date2 = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                date2 = date2 + o
                if row[-2] != '':
                    date3 = datetime.datetime.strptime(row[-2], '%Y-%m-%d %H:%M:%S')
                else:
                    date3 = datetime.datetime.strptime(row[-3], '%Y-%m-%d %H:%M:%S')
                date3 = date3 - o
                if date2 < date1 and date1 < date3:
                    num = num + 1
            numda.append(srr)
            numda.append(date1.strftime('%Y-%m-%d-%H-%M'))
            numda.append(num)
            numdae.append(numda)
        pd.DataFrame(np.array(numdae), columns=['quyu', 'time', 'num']).to_csv(
            '../pjf_data/train_num_%s.csv' % srr, index=False)
allimr = []
for j in range(15, 18):
     for g in range(0, 60):
         ime = "2016-09-%d-%d-%d" % (25, j, g)
         allimr.append(ime)
for j in range(0, 2):
    for g in range(1, 4):
        numdae = []
        if j == 0:
            srr = 'E%d' % g;
        if j == 1:
            srr = 'W%d' % g
        for i in allimr:
            date1 = datetime.datetime.strptime(i, '%Y-%m-%d-%H-%M')
            o = datetime.timedelta(hours=0.2)
            f = open("../pjf_data/%s.csv" % srr);
            rows = csv.reader(f)
            rows.next()
            num = 0
            for row in rows:
                numda = []
                date2 = datetime.datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                date2 = date2 + o
                if row[-2] != '':
                    date3 = datetime.datetime.strptime(row[-2], '%Y-%m-%d %H:%M:%S')
                else:
                    date3 = datetime.datetime.strptime(row[-3], '%Y-%m-%d %H:%M:%S')
                date3 = date3 - o
                if date2 < date1 and date1 < date3:
                    num = num + 1
            numda.append(srr)
            numda.append(date1.strftime('%Y-%m-%d-%H-%M'))
            numda.append(num)
            numdae.append(numda)
        pd.DataFrame(np.array(numdae), columns=['quyu', 'time', 'num']).to_csv(
            '../pjf_data/test_num_%s.csv' % srr, index=False)