__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os
time_dict = {}
rows = csv.reader(open('../ori_data/airport_gz_security_check_chusai_1stround.csv','rb'))
rows.next()
for row in rows:
        time_stamp = row[1][:-4]
        time_stamp += "0"
        if time_stamp in time_dict:
            time_dict[time_stamp] += 1
        else:
            time_dict[time_stamp] = 1

print "writting..."
time_stamp_list = []
# time_stamp_sublist = []
for time_stamp in time_dict:
    time_stamp_sublist=[time_dict[time_stamp],time_stamp]
    time_stamp_list.append(time_stamp_sublist)
    # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
pd.DataFrame(time_stamp_list)
f = open("../merge_10_check/checkin.csv", "wb")
write = csv.writer(f)
write.writerow(["passengerCount", "timeStamp"])
write.writerows(time_stamp_list)
f.close()