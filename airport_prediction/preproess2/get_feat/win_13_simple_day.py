__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os
import cPickle
time_stamp_dict={}
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)

for file_name in file_list:
    print file_name
    time_dict = {}
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            time_stamp = row[1].split(" ")[1]
            data=float(row[0])
            date = row[1].split(" ")[0][8:10]
            time_stamp=date+"-"+time_stamp
            file = file_name.split(".")[0]
            if int(date)>=11 or file =='84'or file =='160'\
                    or file =='292'or file =='347'or file =='385'\
                    or file =='471'or file =='499'or file =='596':
                if time_stamp in time_dict:
                    time_dict[time_stamp] += data
                else:
                    time_dict[time_stamp] = data


    print "writting..."
    print wifi_name_dict[int(file_name.split(".")[0])]
    print file_name
    time_stamp_list = []
    # time_stamp_sublist = []
    for time_stamp in time_dict:
        time_stamp_sublist=[float(time_dict[time_stamp]),time_stamp]

        data = time_stamp.split("-")[0]+"-"
        if time_stamp==data+'15:00':
            time_stamp1=data+'14:00'
            time_stamp2=data+'14:10'
            time_stamp3=data+'14:20'
            time_stamp4=data+'14:30'
            time_stamp5=data+'14:40'
            time_stamp6=data+'14:50'
            time_stamp7=data+'15:10'
            time_stamp8=data+'15:20'
            time_stamp9=data+'15:30'
            time_stamp10=data+'15:40'
            time_stamp11=data+'15:50'
            time_stamp12=data+'16:00'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"1"
            time_stamp_dict[key]=dat
        if time_stamp==data+'15:10':
            time_stamp1=data+'14:10'
            time_stamp2=data+'14:20'
            time_stamp3=data+'14:30'
            time_stamp4=data+'14:40'
            time_stamp5=data+'14:50'
            time_stamp6=data+'15:00'
            time_stamp7=data+'15:20'
            time_stamp8=data+'15:30'
            time_stamp9=data+'15:40'
            time_stamp10=data+'15:50'
            time_stamp11=data+'16:00'
            time_stamp12=data+'16:10'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"2"
            time_stamp_dict[key]=dat
        if time_stamp==data+'15:20':
            time_stamp1=data+'16:20'
            time_stamp2=data+'14:20'
            time_stamp3=data+'14:30'
            time_stamp4=data+'14:40'
            time_stamp5=data+'14:50'
            time_stamp6=data+'15:00'
            time_stamp7=data+'15:10'
            time_stamp8=data+'15:30'
            time_stamp9=data+'15:40'
            time_stamp10=data+'15:50'
            time_stamp11=data+'16:00'
            time_stamp12=data+'16:10'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"3"
            time_stamp_dict[key]=dat
        if time_stamp==data+'15:30':
            time_stamp1=data+'14:30'
            time_stamp2=data+'14:40'
            time_stamp3=data+'14:50'
            time_stamp4=data+'15:00'
            time_stamp5=data+'15:10'
            time_stamp6=data+'15:20'
            time_stamp7=data+'15:40'
            time_stamp8=data+'15:50'
            time_stamp9=data+'16:00'
            time_stamp10=data+'16:10'
            time_stamp11=data+'16:20'
            time_stamp12=data+'16:30'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"4"
            time_stamp_dict[key]=dat
        if time_stamp==data+'15:40':
            time_stamp1=data+'14:40'
            time_stamp2=data+'14:50'
            time_stamp3=data+'15:00'
            time_stamp4=data+'15:10'
            time_stamp5=data+'15:20'
            time_stamp6=data+'15:30'
            time_stamp7=data+'15:50'
            time_stamp8=data+'16:00'
            time_stamp9=data+'16:10'
            time_stamp10=data+'16:20'
            time_stamp11=data+'16:30'
            time_stamp12=data+'16:40'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"5"
            time_stamp_dict[key]=dat
        if time_stamp==data+'15:50':
            time_stamp1=data+'14:50'
            time_stamp2=data+'15:00'
            time_stamp3=data+'15:10'
            time_stamp4=data+'15:20'
            time_stamp5=data+'15:30'
            time_stamp6=data+'15:40'
            time_stamp7=data+'16:00'
            time_stamp8=data+'16:10'
            time_stamp9=data+'16:20'
            time_stamp10=data+'16:30'
            time_stamp11=data+'16:40'
            time_stamp12=data+'16:50'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"6"
            time_stamp_dict[key]=dat
        if time_stamp==data+'16:00':
            time_stamp1=data+'15:00'
            time_stamp2=data+'15:10'
            time_stamp3=data+'15:20'
            time_stamp4=data+'15:30'
            time_stamp5=data+'15:40'
            time_stamp6=data+'15:50'
            time_stamp7=data+'16:10'
            time_stamp8=data+'16:20'
            time_stamp9=data+'16:30'
            time_stamp10=data+'16:40'
            time_stamp11=data+'16:50'
            time_stamp12=data+'17:00'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"7"
            time_stamp_dict[key]=dat
        if time_stamp==data+'16:10':
            time_stamp1=data+'15:10'
            time_stamp2=data+'15:20'
            time_stamp3=data+'15:30'
            time_stamp4=data+'15:40'
            time_stamp5=data+'15:50'
            time_stamp6=data+'16:00'
            time_stamp7=data+'16:20'
            time_stamp8=data+'16:30'
            time_stamp9=data+'16:40'
            time_stamp10=data+'16:50'
            time_stamp11=data+'17:00'
            time_stamp12=data+'17:10'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"8"
            time_stamp_dict[key]=dat
        if time_stamp==data+'16:20':
            time_stamp1=data+'15:20'
            time_stamp2=data+'15:30'
            time_stamp3=data+'15:40'
            time_stamp4=data+'15:50'
            time_stamp5=data+'16:00'
            time_stamp6=data+'16:10'
            time_stamp7=data+'16:30'
            time_stamp8=data+'16:40'
            time_stamp9=data+'16:50'
            time_stamp10=data+'17:00'
            time_stamp11=data+'17:10'
            time_stamp12=data+'17:20'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"9"
            time_stamp_dict[key]=dat
            if int(file_name.split(".")[0])==1 and time_stamp.split("-")[0]=='20':
                print "asdasdsada",key
            if key =="WC-3C<WC-3-13>-20-9":
                print "23455666666666"
        if time_stamp==data+'16:30':
            time_stamp1=data+'15:30'
            time_stamp2=data+'15:40'
            time_stamp3=data+'15:50'
            time_stamp4=data+'16:00'
            time_stamp5=data+'16:10'
            time_stamp6=data+'16:20'
            time_stamp7=data+'16:40'
            time_stamp8=data+'16:50'
            time_stamp9=data+'17:00'
            time_stamp10=data+'17:10'
            time_stamp11=data+'17:20'
            time_stamp12=data+'17:30'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"10"
            time_stamp_dict[key]=dat
        if time_stamp==data+'16:40':
            time_stamp1=data+'15:40'
            time_stamp2=data+'15:50'
            time_stamp3=data+'16:00'
            time_stamp4=data+'16:10'
            time_stamp5=data+'16:20'
            time_stamp6=data+'16:30'
            time_stamp7=data+'16:50'
            time_stamp8=data+'17:00'
            time_stamp9=data+'17:10'
            time_stamp10=data+'17:20'
            time_stamp11=data+'17:30'
            time_stamp12=data+'17:40'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"11"
            time_stamp_dict[key]=dat
        if time_stamp==data+'16:50':
            time_stamp1=data+'15:50'
            time_stamp2=data+'16:00'
            time_stamp3=data+'16:10'
            time_stamp4=data+'16:20'
            time_stamp5=data+'16:30'
            time_stamp6=data+'16:40'
            time_stamp7=data+'17:00'
            time_stamp8=data+'17:10'
            time_stamp9=data+'17:20'
            time_stamp10=data+'17:30'
            time_stamp11=data+'17:40'
            time_stamp12=data+'17:50'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"12"
            time_stamp_dict[key]=dat
        if time_stamp==data+'17:00':
            time_stamp1=data+'16:00'
            time_stamp2=data+'16:10'
            time_stamp3=data+'16:20'
            time_stamp4=data+'16:30'
            time_stamp5=data+'16:40'
            time_stamp6=data+'16:50'
            time_stamp7=data+'17:10'
            time_stamp8=data+'17:20'
            time_stamp9=data+'17:30'
            time_stamp10=data+'17:40'
            time_stamp11=data+'17:50'
            time_stamp12=data+'18:00'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"13"
            time_stamp_dict[key]=dat
        if time_stamp==data+'17:10':
            time_stamp1=data+'16:10'
            time_stamp2=data+'16:20'
            time_stamp3=data+'16:30'
            time_stamp4=data+'16:40'
            time_stamp5=data+'16:50'
            time_stamp6=data+'17:00'
            time_stamp7=data+'17:20'
            time_stamp8=data+'17:30'
            time_stamp9=data+'17:40'
            time_stamp10=data+'17:50'
            time_stamp11=data+'18:00'
            time_stamp12=data+'18:10'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"14"
            time_stamp_dict[key]=dat
        if time_stamp==data+'17:20':
            time_stamp1=data+'16:20'
            time_stamp2=data+'16:30'
            time_stamp3=data+'16:40'
            time_stamp4=data+'16:50'
            time_stamp5=data+'17:00'
            time_stamp6=data+'17:10'
            time_stamp7=data+'17:30'
            time_stamp8=data+'17:40'
            time_stamp9=data+'17:50'
            time_stamp10=data+'18:00'
            time_stamp11=data+'18:10'
            time_stamp12=data+'18:20'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"15"
            time_stamp_dict[key]=dat
        if time_stamp==data+'17:30':
            time_stamp1=data+'16:30'
            time_stamp2=data+'16:40'
            time_stamp3=data+'16:50'
            time_stamp4=data+'17:00'
            time_stamp5=data+'17:10'
            time_stamp6=data+'17:20'
            time_stamp7=data+'17:40'
            time_stamp8=data+'17:50'
            time_stamp9=data+'18:00'
            time_stamp10=data+'18:10'
            time_stamp11=data+'18:20'
            time_stamp12=data+'18:30'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"16"
            time_stamp_dict[key]=dat
        if time_stamp==data+'17:40':
            time_stamp1=data+'16:40'
            time_stamp2=data+'16:50'
            time_stamp3=data+'17:00'
            time_stamp4=data+'17:10'
            time_stamp5=data+'17:20'
            time_stamp6=data+'17:30'
            time_stamp7=data+'17:50'
            time_stamp8=data+'18:00'
            time_stamp9=data+'18:10'
            time_stamp10=data+'18:20'
            time_stamp11=data+'18:30'
            time_stamp12=data+'18:40'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"17"
            time_stamp_dict[key]=dat
        if time_stamp==data+'17:50':
            time_stamp1=data+'16:50'
            time_stamp2=data+'17:00'
            time_stamp3=data+'17:10'
            time_stamp4=data+'17:20'
            time_stamp5=data+'17:30'
            time_stamp6=data+'17:40'
            time_stamp7=data+'18:00'
            time_stamp8=data+'18:10'
            time_stamp9=data+'18:20'
            time_stamp10=data+'18:30'
            time_stamp11=data+'18:40'
            time_stamp12=data+'18:50'
            dat=(float(time_dict[time_stamp])+\
            float(time_dict[time_stamp5])+\
            float(time_dict[time_stamp6])+\
            float(time_dict[time_stamp7])+\
            float(time_dict[time_stamp8]))/5
            key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"18"
            time_stamp_dict[key]=dat
        # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
f = open("../simple_win_5_mean_ori.pkl",'wb')
cPickle.dump(time_stamp_dict,f,-1)
f.close()
# f = open("../qianhou1/"+file_name, "wb")
# write = csv.writer(f)
# write.writerow(["passengerCount", "timeStamp"])
# write.writerows(time_stamp_list)
# f.close()