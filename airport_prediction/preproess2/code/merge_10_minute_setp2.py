__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os

direction = "../data/"
file_list = os.listdir(direction)

for file_name in file_list:
    time_dict = {}
    time_count_dict = {}
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            time_stamp= row[1][:-4]
            filter_time_0911 = row[1].split(" ")[0]
            time_stamp+="0"
            data=int(row[0])
            if time_stamp in time_dict:
                time_dict[time_stamp] += data
                time_count_dict[time_stamp] +=1
            else:
                time_dict[time_stamp] = data
                time_count_dict[time_stamp] =1
            print time_count_dict[time_stamp]
    print "writting..."
    time_stamp_list = []
    # time_stamp_sublist = []
    for time_stamp in time_dict:
        time_stamp_sublist=[float(time_dict[time_stamp])/time_count_dict[time_stamp],time_stamp]
        time_stamp_list.append(time_stamp_sublist)
        # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
    pd.DataFrame(time_stamp_list)
    f = open("../merge_10/"+file_name, "wb")
    write = csv.writer(f)
    write.writerow(["passengerCount", "timeStamp"])
    write.writerows(time_stamp_list)
    f.close()