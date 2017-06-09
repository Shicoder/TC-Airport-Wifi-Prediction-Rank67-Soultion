__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os

direction = "../merge_10_with8/"
file_list = os.listdir(direction)

for file_name in file_list:

    time_dict = {}
    time_count_dict = {}
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:

            time_stamp = row[1].split(" ")[1]
            data=float(row[0])
            date = row[1].split(" ")[0][8:10]
            file_one = file_name.split(".")[0]
            if int(date)>=17 or file_one =='84'or file_one =='160'\
                    or file_one =='292'or file_one =='347'or file_one =='385'\
                    or file_one =='471'or file_one =='499'or file_one =='596':
                if time_stamp in time_dict:
                    time_dict[time_stamp] += data
                    time_count_dict[time_stamp] +=1
                else:
                    time_dict[time_stamp] = data
                    time_count_dict[time_stamp] =1


    print "writting..."

    time_stamp_list = []
    # time_stamp_sublist = []
    for time_stamp in time_dict:
        time_stamp_sublist=[float(time_dict[time_stamp])/time_count_dict[time_stamp],time_stamp]

        if time_stamp=='15:00':
            time_stamp1='14:00'
            time_stamp2='14:10'
            time_stamp3='14:20'
            time_stamp4='14:30'
            time_stamp5='14:40'
            time_stamp6='14:50'
            time_stamp7='15:10'
            time_stamp8='15:20'
            time_stamp9='15:30'
            time_stamp10='15:40'
            time_stamp11='15:50'
            time_stamp12='16:00'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:10':
            time_stamp1='14:10'
            time_stamp2='14:20'
            time_stamp3='14:30'
            time_stamp4='14:40'
            time_stamp5='14:50'
            time_stamp6='15:00'
            time_stamp7='15:20'
            time_stamp8='15:30'
            time_stamp9='15:40'
            time_stamp10='15:50'
            time_stamp11='16:00'
            time_stamp12='16:10'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:20':
            time_stamp1='16:20'
            time_stamp2='14:20'
            time_stamp3='14:30'
            time_stamp4='14:40'
            time_stamp5='14:50'
            time_stamp6='15:00'
            time_stamp7='15:10'
            time_stamp8='15:30'
            time_stamp9='15:40'
            time_stamp10='15:50'
            time_stamp11='16:00'
            time_stamp12='16:10'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:30':
            time_stamp1='14:30'
            time_stamp2='14:40'
            time_stamp3='14:50'
            time_stamp4='15:00'
            time_stamp5='15:10'
            time_stamp6='15:20'
            time_stamp7='15:40'
            time_stamp8='15:50'
            time_stamp9='16:00'
            time_stamp10='16:10'
            time_stamp11='16:20'
            time_stamp12='16:30'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:40':
            time_stamp1='14:40'
            time_stamp2='14:50'
            time_stamp3='15:00'
            time_stamp4='15:10'
            time_stamp5='15:20'
            time_stamp6='15:30'
            time_stamp7='15:50'
            time_stamp8='16:00'
            time_stamp9='16:10'
            time_stamp10='16:20'
            time_stamp11='16:30'
            time_stamp12='16:40'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:50':
            time_stamp1='14:50'
            time_stamp2='15:00'
            time_stamp3='15:10'
            time_stamp4='15:20'
            time_stamp5='15:30'
            time_stamp6='15:40'
            time_stamp7='16:00'
            time_stamp8='16:10'
            time_stamp9='16:20'
            time_stamp10='16:30'
            time_stamp11='16:40'
            time_stamp12='16:50'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:00':
            time_stamp1='15:00'
            time_stamp2='15:10'
            time_stamp3='15:20'
            time_stamp4='15:30'
            time_stamp5='15:40'
            time_stamp6='15:50'
            time_stamp7='16:10'
            time_stamp8='16:20'
            time_stamp9='16:30'
            time_stamp10='16:40'
            time_stamp11='16:50'
            time_stamp12='17:00'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:10':
            time_stamp1='15:10'
            time_stamp2='15:20'
            time_stamp3='15:30'
            time_stamp4='15:40'
            time_stamp5='15:50'
            time_stamp6='16:00'
            time_stamp7='16:20'
            time_stamp8='16:30'
            time_stamp9='16:40'
            time_stamp10='16:50'
            time_stamp11='17:00'
            time_stamp12='17:10'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:20':
            time_stamp1='15:20'
            time_stamp2='15:30'
            time_stamp3='15:40'
            time_stamp4='15:50'
            time_stamp5='16:00'
            time_stamp6='16:10'
            time_stamp7='16:30'
            time_stamp8='16:40'
            time_stamp9='16:50'
            time_stamp10='17:00'
            time_stamp11='17:10'
            time_stamp12='17:20'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:30':
            time_stamp1='15:30'
            time_stamp2='15:40'
            time_stamp3='15:50'
            time_stamp4='16:00'
            time_stamp5='16:10'
            time_stamp6='16:20'
            time_stamp7='16:40'
            time_stamp8='16:50'
            time_stamp9='17:00'
            time_stamp10='17:10'
            time_stamp11='17:20'
            time_stamp12='17:30'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:40':
            time_stamp1='15:40'
            time_stamp2='15:50'
            time_stamp3='16:00'
            time_stamp4='16:10'
            time_stamp5='16:20'
            time_stamp6='16:30'
            time_stamp7='16:50'
            time_stamp8='17:00'
            time_stamp9='17:10'
            time_stamp10='17:20'
            time_stamp11='17:30'
            time_stamp12='17:40'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:50':
            time_stamp1='15:50'
            time_stamp2='16:00'
            time_stamp3='16:10'
            time_stamp4='16:20'
            time_stamp5='16:30'
            time_stamp6='16:40'
            time_stamp7='17:00'
            time_stamp8='17:10'
            time_stamp9='17:20'
            time_stamp10='17:30'
            time_stamp11='17:40'
            time_stamp12='17:50'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:00':
            time_stamp1='16:00'
            time_stamp2='16:10'
            time_stamp3='16:20'
            time_stamp4='16:30'
            time_stamp5='16:40'
            time_stamp6='16:50'
            time_stamp7='17:10'
            time_stamp8='17:20'
            time_stamp9='17:30'
            time_stamp10='17:40'
            time_stamp11='17:50'
            time_stamp12='18:00'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:10':
            time_stamp1='16:10'
            time_stamp2='16:20'
            time_stamp3='16:30'
            time_stamp4='16:40'
            time_stamp5='16:50'
            time_stamp6='17:00'
            time_stamp7='17:20'
            time_stamp8='17:30'
            time_stamp9='17:40'
            time_stamp10='17:50'
            time_stamp11='18:00'
            time_stamp12='18:10'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:20':
            time_stamp1='16:20'
            time_stamp2='16:30'
            time_stamp3='16:40'
            time_stamp4='16:50'
            time_stamp5='17:00'
            time_stamp6='17:10'
            time_stamp7='17:30'
            time_stamp8='17:40'
            time_stamp9='17:50'
            time_stamp10='18:00'
            time_stamp11='18:10'
            time_stamp12='18:20'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:30':
            time_stamp1='16:30'
            time_stamp2='16:40'
            time_stamp3='16:50'
            time_stamp4='17:00'
            time_stamp5='17:10'
            time_stamp6='17:20'
            time_stamp7='17:40'
            time_stamp8='17:50'
            time_stamp9='18:00'
            time_stamp10='18:10'
            time_stamp11='18:20'
            time_stamp12='18:30'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:40':
            time_stamp1='16:40'
            time_stamp2='16:50'
            time_stamp3='17:00'
            time_stamp4='17:10'
            time_stamp5='17:20'
            time_stamp6='17:30'
            time_stamp7='17:50'
            time_stamp8='18:00'
            time_stamp9='18:10'
            time_stamp10='18:20'
            time_stamp11='18:30'
            time_stamp12='18:40'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:50':
            time_stamp1='16:50'
            time_stamp2='17:00'
            time_stamp3='17:10'
            time_stamp4='17:20'
            time_stamp5='17:30'
            time_stamp6='17:40'
            time_stamp7='18:00'
            time_stamp8='18:10'
            time_stamp9='18:20'
            time_stamp10='18:30'
            time_stamp11='18:40'
            time_stamp12='18:50'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp1])/time_count_dict[time_stamp1]+\
            float(time_dict[time_stamp2])/time_count_dict[time_stamp2]+\
            float(time_dict[time_stamp3])/time_count_dict[time_stamp3]+\
            float(time_dict[time_stamp4])/time_count_dict[time_stamp4]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8]+\
            float(time_dict[time_stamp9])/time_count_dict[time_stamp9]+\
            float(time_dict[time_stamp10])/time_count_dict[time_stamp10]+\
            float(time_dict[time_stamp11])/time_count_dict[time_stamp11]+\
            float(time_dict[time_stamp12])/time_count_dict[time_stamp12])/13
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        print time_count_dict[time_stamp]
        # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
    pd.DataFrame(time_stamp_list)
    f = open("../win_13_day(19-24)/"+file_name, "wb")
    write = csv.writer(f)
    write.writerow(["passengerCount", "timeStamp"])
    write.writerows(time_stamp_list)
    f.close()