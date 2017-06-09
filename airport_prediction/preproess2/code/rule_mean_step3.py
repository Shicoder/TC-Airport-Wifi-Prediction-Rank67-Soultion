__author__ = 'shi'
#-*-coding:utf-8-*-
"""shao 8ge wenjian"""
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
            date = row[1].split(" ")[0][8:10]
            time_stamp = row[1].split(" ")[1]
            data=float(row[0])
            file_one = file_name.split(".")[0]
            if int(date)>17 or file_one =='84'or file_one =='160'\
                    or file_one =='292'or file_one =='347'or file_one =='385'\
                    or file_one =='471'or file_one =='499'or file_one =='596':
                print date
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

        if time_stamp=='15:00' or time_stamp=='15:10' or time_stamp=='15:20' or time_stamp=='15:30' or\
                        time_stamp=='15:40'or time_stamp=='15:50'or time_stamp=='16:00'or time_stamp=='16:10'or\
               time_stamp=='16:20'or time_stamp=='16:30'or time_stamp=='16:40'or time_stamp=='16:50'or \
               time_stamp=='17:00'or time_stamp=='17:10'or time_stamp=='17:20'or time_stamp=='17:30'or\
               time_stamp=='17:40'or time_stamp=='17:50':
            time_stamp_list.append(time_stamp_sublist)
            print time_count_dict[time_stamp]
        # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
    pd.DataFrame(time_stamp_list)
    f = open("../result_simple_dot_mean/"+file_name, "wb")
    write = csv.writer(f)
    write.writerow(["passengerCount", "timeStamp"])
    write.writerows(time_stamp_list)
    f.close()