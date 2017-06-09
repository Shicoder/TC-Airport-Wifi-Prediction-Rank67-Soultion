#-*-coding:utf-8-*-
import csv
import time,datetime
import os
import pandas as pd
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
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
for g in range(len(arealist)):
    daadic={}
    srr=arealist[g]
    f = open("D:/Shi/python/3/10_19/aindaa/%s.csv" % srr);
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        daadic[row[0]]=row[1]
    ainds=[]
    f = open("D:/Shi/python/3/10_19/train_feat.csv");
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        aind=[]
        if daadic.has_key(row[0]):
            aind=row
            aind.append(daadic[row[0]])
            ainds.append(aind)
        else:
            aind = row
            aind.append(0)
            ainds.append(aind)
    pd.DataFrame(np.array(ainds)).to_csv('D:/Shi/python/3/10_19/train_feat.csv',index=False,header=None)

for g in range(len(arealist)):
    daadic={}
    srr=arealist[g]
    f = open("D:/Shi/python/3/10_19/esdaa/%s.csv" % srr);
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        daadic[row[0]]=row[1]
    ainds=[]
    f = open("D:/Shi/python/3/10_19/gbdt_feat_target.csv");
    rows = csv.reader(f)
    rows.next()
    for row in rows:
        aind=[]
        if daadic.has_key(row[0]):
            aind=row
            aind.append(daadic[row[0]])
            ainds.append(aind)
        else:
            aind = row
            aind.append(0)
            ainds.append(aind)
    pd.DataFrame(np.array(ainds)).to_csv('D:/Shi/python/3/10_19/gbdt_feat_target.csv',index=False,header=None)

# train_feat = pd.read_csv('d:/fligh/10_19/train_feat.csv', sep=',', index_col='BGATEtime')
# gbdt_feat_target = pd.read_csv('d:/fligh/10_19/gbdt_feat_target.csv', sep=',', index_col='BGATEtime')
# for g in range(0, len(arealist)):
#     train= pd.read_csv('d:/fligh/10_19/aindaa/%s.csv'%arealist[g], sep=',',index_col='BGATEtime')
#     gbdt_feat= pd.read_csv('d:/fligh/10_19/esdaa/%s.csv'%arealist[g], sep=',',index_col='BGATEtime')
#     train_feat=train_feat.join(train)
#     gbdt_feat_target=gbdt_feat_target.join(gbdt_feat)
# train_feat.fillna(0)
# gbdt_feat_target.fillna(0)
# train_feat.to_csv("d:/fligh/10_19/train_feat2.csv",index=False,header=None)
# gbdt_feat_target.to_csv("d:/fligh/10_19/gbdt_feat_target2.csv",index=False,header=None)
#         numdae = []
#         num = 1
#         sum = 0
#         srr = arealist[g]
#         f = open("D:/fligh/aindaa/train_num_%s.csv" % srr);
#         rows = csv.reader(f)
#         rows.next()
#
#         for row in rows:
#             sum = sum + int(row[3])
#             if num==10:
#                 num=1
#                 numda=[]
#                 numag=float(sum/10.00)
#                 sum=0
#                 numda.append(row[1]+row[2].split('-')[0]+'-'+row[2].split('-')[1]+'-'+row[2].split('-')[2]+'-'+row[2].split('-')[3]+'-'+row[2].split('-')[4][0])
#                 numda.append(numag)
#                 numdae.append(numda)
#                 # print numdae
#             num = num + 1
#         pd.DataFrame(np.array(numdae), columns=[ 'BGATEtime',srr ]).to_csv('d:/fligh/10_19/aindaa/%s.csv' % srr, index=False)
#
#
# for g in range(0, len(arealist)):
#         numdae = []
#         num = 1
#         sum = 0
#         srr = arealist[g]
#         f = open("D:/fligh/esdaa/test_num_%s.csv" % srr);
#         rows = csv.reader(f)
#         rows.next()
#
#         for row in rows:
#             sum = sum + int(row[3])
#             if num==10:
#                 num=1
#                 numda=[]
#                 numag=float(sum/10.00)
#                 sum=0
#                 numda.append(row[1]+row[2].split('-')[0]+'-'+row[2].split('-')[1]+'-'+row[2].split('-')[2]+'-'+row[2].split('-')[3]+'-'+row[2].split('-')[4][0])
#                 numda.append(numag)
#                 numdae.append(numda)
#             num = num + 1
#         pd.DataFrame(np.array(numdae), columns=[ 'BGATEtime', srr]).to_csv( 'd:/fligh/10_19/esdaa/%s.csv' % srr, index=False)

