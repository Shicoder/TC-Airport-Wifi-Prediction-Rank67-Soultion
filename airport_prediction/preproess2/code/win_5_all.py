__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os

def median(lst):
    if not lst:
        return
    lst=sorted(lst)
    if len(lst)%2==1:
        return lst[len(lst)/2]
    else:
        return  (lst[len(lst)//2-1]+lst[len(lst//2)])/2.0
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
            time_stamp5='14:40'
            time_stamp6='14:50'
            time_stamp7='15:10'
            time_stamp8='15:20'
            median_list=[float(time_dict[time_stamp]),float(time_dict[time_stamp5]),float(time_dict[time_stamp6]),
                         float(time_dict[time_stamp7]),float(time_dict[time_stamp8])]
            dat=median(median_list)
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:10':
            time_stamp5='14:50'
            time_stamp6='15:00'
            time_stamp7='15:20'
            time_stamp8='15:30'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:20':
            time_stamp6='15:00'
            time_stamp7='15:10'
            time_stamp8='15:30'
            time_stamp9='15:40'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:30':
            time_stamp5='15:10'
            time_stamp6='15:20'
            time_stamp7='15:40'
            time_stamp8='15:50'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:40':
            time_stamp5='15:20'
            time_stamp6='15:30'
            time_stamp7='15:50'
            time_stamp8='16:00'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='15:50':
            time_stamp5='15:30'
            time_stamp6='15:40'
            time_stamp7='16:00'
            time_stamp8='16:10'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:00':
            time_stamp5='15:40'
            time_stamp6='15:50'
            time_stamp7='16:10'
            time_stamp8='16:20'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:10':
            time_stamp5='15:50'
            time_stamp6='16:00'
            time_stamp7='16:20'
            time_stamp8='16:30'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:20':
            time_stamp5='16:00'
            time_stamp6='16:10'
            time_stamp7='16:30'
            time_stamp8='16:40'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:30':
            time_stamp5='16:10'
            time_stamp6='16:20'
            time_stamp7='16:40'
            time_stamp8='16:50'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:40':
            time_stamp5='16:20'
            time_stamp6='16:30'
            time_stamp7='16:50'
            time_stamp8='17:00'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='16:50':
            time_stamp5='16:30'
            time_stamp6='16:40'
            time_stamp7='17:00'
            time_stamp8='17:10'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:00':
            time_stamp5='16:40'
            time_stamp6='16:50'
            time_stamp7='17:10'
            time_stamp8='17:20'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:10':
            time_stamp5='16:50'
            time_stamp6='17:00'
            time_stamp7='17:20'
            time_stamp8='17:30'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:20':
            time_stamp5='17:00'
            time_stamp6='17:10'
            time_stamp7='17:30'
            time_stamp8='17:40'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:30':
            time_stamp5='17:10'
            time_stamp6='17:20'
            time_stamp7='17:40'
            time_stamp8='17:50'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:40':
            time_stamp5='17:20'
            time_stamp6='17:30'
            time_stamp7='17:50'
            time_stamp8='18:00'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        if time_stamp=='17:50':
            time_stamp5='17:30'
            time_stamp6='17:40'
            time_stamp7='18:00'
            time_stamp8='18:10'
            data=(float(time_dict[time_stamp])/time_count_dict[time_stamp]+\
            float(time_dict[time_stamp5])/time_count_dict[time_stamp5]+\
            float(time_dict[time_stamp6])/time_count_dict[time_stamp6]+\
            float(time_dict[time_stamp7])/time_count_dict[time_stamp7]+\
            float(time_dict[time_stamp8])/time_count_dict[time_stamp8])/5
            time_stamp_sublist=[data,time_stamp]
            time_stamp_list.append(time_stamp_sublist)
        print time_count_dict[time_stamp]
        # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
    pd.DataFrame(time_stamp_list)
    f = open("../win_5_day(19-24)/"+file_name, "wb")
    write = csv.writer(f)
    write.writerow(["passengerCount", "timeStamp"])
    write.writerows(time_stamp_list)
    f.close()