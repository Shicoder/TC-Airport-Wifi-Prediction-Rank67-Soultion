#-*-coding:utf-8-*-
import csv
import time,datetime
import os
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
allimr = []
for i in range(17,25):
   for j in range(15,18):
       for g in range(0,60):
        ime = "2016-09-%d-%d-%d"%(i,j,g)
        allimr.append(ime)
arealist=['A10','A114','B214','B215','B216','B217','B219','B220','B221','B222','B223','B224','B225',
'B226','B227','B228','B229','B230','B231','B232','B233','B234','B235',
'B901','B902','B903','B904','B906','B907','B908','B909']
# pd.DataFrame(np.array(allimr), columns=['time']).to_csv('d:/fligh/10_17/time.csv', index=False)
# joinanjianpeonum=pd.read_csv('d:/fligh/10_17/joinanjianpeonum.csv',sep=',')
# for name,group in joinanjianpeonum.groupby('BGATE_AREA'):
#     group.to_csv("d:/fligh/10_17/%s.csv"%name,index=False)

import csv
import time, datetime
import os


for g in range(0, len(arealist)):
        numdae = []
        srr = arealist[g]
        for i in allimr:
            date1 = datetime.datetime.strptime(i, '%Y-%m-%d-%H-%M')
            o = datetime.timedelta(hours=0.2)
            f = open("../BGATE_ID/%s.csv" % srr);
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
            numda.append(row[-1])
            numda.append(date1.strftime('%Y-%m-%d-%H-%M'))
            numda.append(num)
            numdae.append(numda)
        pd.DataFrame(np.array(numdae), columns=['BGATE_ID','BGATE_AREA', 'time', 'num']).to_csv('../pjf_test/train_num_%s.csv' % srr, index=False)
allimr = []
arealist=['A01','A02','A03','A04','A05',
'A11','A13','A14','A15','A16','A17','A18',
'A101','A102','A103','A104','A105','A106','A108','A109',
'A110','A115','A116','A117','A118','A119',
'A120','A121','A122','A123','A124','A125','A126','A127','A128','A129',
'A130','A131','A132','A133',
'B02','B03','B04','B08','B09','B10','B13','B14','B15','B16','B17','B18',
'B201','B202','B203','B204','B206','B207','B208','B209','B210','B212','B213',
'A10','A114','B214','B215','B216','B217','B219','B220','B221','B222','B223','B224','B225',
'B226','B227','B228','B229','B230','B231','B232','B233','B234','B235',
'B901','B902','B903','B904','B906','B907','B908','B909']
for j in range(15, 18):
     for g in range(0, 60):
         ime = "2016-09-%d-%d-%d" % (25, j, g)
         allimr.append(ime)
for g in range(0, len(arealist)):
        numdae = []
        srr = arealist[g]
        for i in allimr:
            date1 = datetime.datetime.strptime(i, '%Y-%m-%d-%H-%M')
            o = datetime.timedelta(hours=0.2)
            f = open("../BGATE_ID/%s.csv" % srr);
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
            numda.append(row[-1])
            numda.append(date1.strftime('%Y-%m-%d-%H-%M'))
            numda.append(num)
            numdae.append(numda)
        pd.DataFrame(np.array(numdae), columns=['BGATE_ID','BGATE_AREA', 'time', 'num']).to_csv('../pjf_test/test_num_%s.csv' % srr, index=False)