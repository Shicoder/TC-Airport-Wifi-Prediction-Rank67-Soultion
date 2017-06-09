#-*-coding:utf-8-*-
import csv
import time,datetime
import os
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
# f = open("D:/fligh/10_21/wifi_avg.txt" );
# rows = csv.reader(f)
# rows.next()
# wifi_tag={}
# num=1
# for row in rows:
#     if wifi_tag.has_key(row[0]):
#         continue
#     else:
#         if num==88:
#             print row[0]
#         wifi_tag[row[0]]=num
#         num=num+1


# # f = open("D:/fligh/10_21/wifi_avg.txt" );
# # rows = csv.reader(f)
# # rows.next()
# # listwifi=[]
# # for row in rows:
# #     listwifi.append([wifi_tag[row[0]],row[1],row[2]])
# # flighda = pd.DataFrame(np.array(listwifi),columns=['wifi','time','p'])
# # flighda.to_csv("D:/fligh/10_21/wifi_avggaibian.txt",sep=',',index=False)
#
# f = open("D:/fligh/10_21/predict_xgboost_best.csv" );
# rows = csv.reader(f)
# rows.next()
# listwifi=[]
# for row in rows:
#     listwifi.append([wifi_tag[row[0]],row[1],row[3]])
# flighda = pd.DataFrame(np.array(listwifi),columns=['wifi','time','p'])
# # flighda.to_csv("D:/fligh/10_21/predict_xgboost_bestgaibian.csv",sep=',',index=False)
# flighwifi = pd.read_csv("D:/fligh/10_21/predict_xgboost_bestgaibian.csv",sep=',')
# wifi =wifi_tag.keys()
# num=0
# for name,group in flighwifi.groupby('wifi'):
#     num = num+1
#     group.to_csv("D:/fligh/10_21/wifi/%s.csv"%name,sep=',',index=False)
# print num

# prewifi = pd.read_csv("D:/fligh/10_21/wifi_avggaibian.txt",sep=',')
# # wifi =wifi_tag.keys()
# for name,group in prewifi.groupby('wifi'):
#     group.to_csv("D:/fligh/10_21/pre/%s.csv"%name,sep=',',index=False)
for i in range(1,750):
    print i
    f = open("../res/%s.csv" % str(i))
    rows = csv.reader(f)
    rows.next()
    listwifi={}
    for row in rows:
            listwifi[row[1].split('-')[2]+'-'+row[1].split('-')[3]+'-'+row[1].split('-')[4]]=row[2]
    allda=[]
    for s in range (10,25):
        sum=0
        for j in range(11,15):
            for z in range(0,6):
                if listwifi.has_key('25-%s-%s'%(j,z)):
                    if listwifi.has_key('%s-%s-%s'%(s,j,z)):
                        sum = sum+(float(listwifi['%s-%s-%s'%(s,j,z)])-float(listwifi['25-%s-%s'%(j,z)]))*\
                                  (float(listwifi['%s-%s-%s'%(s,j,z)])-float(listwifi['25-%s-%s'%(j,z)]))
                    else:
                        tag = '25-'+bytes(j)+'-'+bytes(z)
                        sum = sum+float(listwifi[tag])*float(listwifi[tag])
                else:
                    continue
        allda.append(sum)
    min=100000000000000000
    num=0
    for g in range(0,15):
        if allda[g]<min:
            min = allda[g]
            num = g
        else:
            continue
    print num+10

    # xyic=[]
    # f = open("D:/fligh/10_21/res/%s.csv" % str(i))
    # rows = csv.reader(f)
    # rows.next()
    # for row in rows:
    #     if int(row[1].split('-')[2])==num+10 or int(row[1].split('-')[2])==25:
    #         xyic.append([row[1].split('-')[2]+'-'+row[1].split('-')[3]+'-'+row[1].split('-')[4],float(row[2])])
    #     else:
    #         continue
    # xyic = pd.DataFrame(xyic,columns=['time','p'])
    # print xyic.head()
    # xyic =xyic.set_index('time')
    # xyic.plot()
    # plt.show()
    day = str(num+10)
    xyic=[]
    for h in range(0, 19):
        for y in range(1,6):

            if h<10:
                sh='0'+str(h)
            else:
                sh=str(h)
            sy=str(y)
            if listwifi.has_key(day+ '-' + sh + '-' + sy):
                day1=float(listwifi[day+ '-' + sh + '-' + sy])
            else:
                day1=0.0
            if listwifi.has_key(str(25)+ '-' + sh + '-' + sy):
                day2=float(listwifi[str(25)+ '-' + sh + '-' + sy])
            else:
                day2=0.0

            xyic.append( [sh+':'+sy,day1,day2])

    xyic1 = pd.DataFrame(xyic,columns=['time','p%s'%day,'p25'])
    xyic1 = xyic1.set_index('time')

    day = str(num + 10)
    xyic = []
    for h in range(15, 18):
        for y in range(1, 6):

            if h < 10:
                sh = '0' + str(h)
            else:
                sh = str(h)
            sy = str(y)
            if listwifi.has_key(day + '-' + sh + '-' + sy):
                day1 = float(listwifi[day + '-' + sh + '-' + sy])
            else:
                day1 = 0.0
            if listwifi.has_key(str(25) + '-' + sh + '-' + sy):
                day2 = float(listwifi[str(25) + '-' + sh + '-' + sy])
            else:
                day2 = 0.0

            xyic.append([sh + ':' + sy, day1, day2])

    xyic2 = pd.DataFrame(xyic, columns=['time', 'p%s'%day, 'p25'])
    xyic2 =xyic2.set_index('time')
    xyic1.plot()
    xyic2.plot()
    # fig,axes=plt.subplots(1,2)
    # axes[0,0].plot(xyic1['time'],xyic1['p'],'g--')
    # axes[0, 0].plot(xyic1['p25'])
    # axes[0,1].plot(xyic2['p'])
    # axes[0, 1].plot(xyic2['p25'])
    plt.show()
    print  '========================================'





    # flighwifi = pd.read_csv("D:/fligh/10_21/wifi_1/%s.csv"%str(i), sep=',')
    # flighpre = pd.read_csv("D:/fligh/10_21/pre/%s.csv" % str(i), sep=',')
    # flighwifi = flighwifi.sort('time')
    # flighpre = flighpre.sort('time')
    #
    # flighconcat=pd.concat([flighwifi,flighpre])
    #
    #
    # #print  type(flighconcat)
    # flighconcat.to_csv("D:/fligh/10_21/res/%s.csv"% str(i),sep=',',index=False)
    # print i
    # flighwifi = pd.read_csv("D:/fligh/10_21/res/%s.csv" % str(i), sep=',')
    # flighwifi =flighwifi.set_index('time')
    # flighwifi.plot()
    # plt.show()

# prewifi = pd.read_csv("D:/fligh/10_21/3/reslut_xgboost_10_21_online_addpjf.csv",sep=',')
# num=0
# for name,group in prewifi.groupby('WIFIAPTag'):
#     if(len(group))==18:
#         num=num+1
# print num
