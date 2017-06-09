__author__ = 'shi'
#-*-coding:utf-8-*-

import csv
import pandas as pd
import os
import cPickle
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
time_stamp_dict={}
def median(lst):
    if not lst:
        return
    lst=sorted(lst)
    if len(lst)%2==1:
        return lst[len(lst)/2]
    else:
        return  (lst[len(lst)//2-1]+lst[len(lst//2)])/2.0
direction = "../merge_10/"
file_list = os.listdir(direction)

for file_name in file_list:

    time_dict = {}
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:

            time_stamp = str(int(row[1].split(" ")[1].split(":")[0]))+":"+row[1].split(" ")[1].split(":")[1]
            data=float(row[0])
            date = row[1].split(" ")[0][8:10]
            time_stamp=date+"-"+time_stamp
            file = file_name.split(".")[0]
            if (int(date)>=17 and int(date)<25) or file =='84'or file =='160'\
                    or file =='292'or file =='347'or file =='385'\
                    or file =='471'or file =='499'or file =='596':
                if time_stamp in time_dict:
                    time_dict[time_stamp] += data
                else:
                    time_dict[time_stamp] = data

    print "writting..."
    median_list=[]
    save_list=[]
    time_stamp_list = []
    # time_stamp_sublist = []
    for time_stamp in time_dict:
        print file_name
        time_stamp_sublist=[float(time_dict[time_stamp]),time_stamp]

        data = time_stamp.split("-")[0]+"-"
        for i in range(12):
            time =6+i
            if time_stamp==data+str(time)+':00':
                time_stamp1=data+str(time-1)+':00'
                time_stamp2=data+str(time-1)+':10'
                time_stamp3=data+str(time-1)+':20'
                time_stamp4=data+str(time-1)+':30'
                time_stamp5=data+str(time-1)+':40'
                time_stamp6=data+str(time-1)+':50'
                time_stamp7=data+str(time)+':10'
                time_stamp8=data+str(time)+':20'
                time_stamp9=data+str(time)+':30'
                time_stamp10=data+str(time)+':40'
                time_stamp11=data+str(time)+':50'
                time_stamp12=data+str(time)+':00'
                median_list=[float(time_dict[time_stamp]),float(time_dict[time_stamp3]),float(time_dict[time_stamp4]),
                         float(time_dict[time_stamp5]),float(time_dict[time_stamp6]),float(time_dict[time_stamp7]),
                         float(time_dict[time_stamp8]),float(time_dict[time_stamp9]),float(time_dict[time_stamp10])]
                dat=median(median_list)
                if time<10:
                    pre="2016-09-"+data+" 0"+str(time)+':00'
                else:
                    pre="2016-09-"+data+" "+str(time)+':00'
                save_l=[dat,pre]
                save_list.append(save_l)
                # key = wifi_name_dict[int(file_name.split(".")[0])]+"-"+data+"1"
                #
                # time_stamp_dict[key]=dat
            if time_stamp==data+str(time)+':10':
                time_stamp1=data+str(time-1)+':10'
                time_stamp2=data+str(time-1)+':20'
                time_stamp3=data+str(time-1)+':30'
                time_stamp4=data+str(time-1)+':40'
                time_stamp5=data+str(time-1)+':50'
                time_stamp6=data+str(time)+':00'
                time_stamp7=data+str(time)+':20'
                time_stamp8=data+str(time)+':30'
                time_stamp9=data+str(time)+':40'
                time_stamp10=data+str(time)+':50'
                time_stamp11=data+str(time+1)+':00'
                time_stamp12=data+str(time+1)+':10'
                median_list=[float(time_dict[time_stamp]),float(time_dict[time_stamp3]),float(time_dict[time_stamp4]),
                         float(time_dict[time_stamp5]),float(time_dict[time_stamp6]),float(time_dict[time_stamp7]),
                         float(time_dict[time_stamp8]),float(time_dict[time_stamp9]),float(time_dict[time_stamp10])]
                dat=median(median_list)
                if time<10:
                    pre="2016-09-"+data+" 0"+str(time)+':00'
                else:
                    pre="2016-09-"+data+" "+str(time)+':00'
                save_l=[dat,pre]
                save_list.append(save_l)
            if time_stamp==data+str(time)+':20':
                time_stamp1=data+str(time-1)+':20'
                time_stamp2=data+str(time-1)+':20'
                time_stamp3=data+str(time-1)+':30'
                time_stamp4=data+str(time-1)+':40'
                time_stamp5=data+str(time-1)+':50'
                time_stamp6=data+str(time)+':00'
                time_stamp7=data+str(time)+':10'
                time_stamp8=data+str(time)+':30'
                time_stamp9=data+str(time)+':40'
                time_stamp10=data+str(time)+':50'
                time_stamp11=data+str(time+1)+':00'
                time_stamp12=data+str(time+1)+':10'
                median_list=[float(time_dict[time_stamp]),float(time_dict[time_stamp3]),float(time_dict[time_stamp4]),
                         float(time_dict[time_stamp5]),float(time_dict[time_stamp6]),float(time_dict[time_stamp7]),
                         float(time_dict[time_stamp8]),float(time_dict[time_stamp9]),float(time_dict[time_stamp10])]
                dat=median(median_list)
                if time<10:
                    pre="2016-09-"+data+" 0"+str(time)+':00'
                else:
                    pre="2016-09-"+data+" "+str(time)+':00'
                save_l=[dat,pre]
                save_list.append(save_l)
            if time_stamp==data+str(time)+':30':
                time_stamp1=data+str(time-1)+':30'
                time_stamp2=data+str(time-1)+':40'
                time_stamp3=data+str(time-1)+':50'
                time_stamp4=data+str(time)+':00'
                time_stamp5=data+str(time)+':10'
                time_stamp6=data+str(time)+':20'
                time_stamp7=data+str(time)+':40'
                time_stamp8=data+str(time)+':50'
                time_stamp9=data+str(time+1)+':00'
                time_stamp10=data+str(time+1)+':10'
                time_stamp11=data+str(time+1)+':20'
                time_stamp12=data+str(time+1)+':30'
                median_list=[float(time_dict[time_stamp]),float(time_dict[time_stamp3]),float(time_dict[time_stamp4]),
                         float(time_dict[time_stamp5]),float(time_dict[time_stamp6]),float(time_dict[time_stamp7]),
                         float(time_dict[time_stamp8]),float(time_dict[time_stamp9]),float(time_dict[time_stamp10])]
                dat=median(median_list)
                if time<10:
                    pre="2016-09-"+data+" 0"+str(time)+':00'
                else:
                    pre="2016-09-"+data+" "+str(time)+':00'
                save_l=[dat,pre]
                save_list.append(save_l)
            if time_stamp==data+str(time)+':40':
                time_stamp1=data+str(time-1)+':40'
                time_stamp2=data+str(time-1)+':50'
                time_stamp3=data+str(time)+':00'
                time_stamp4=data+str(time)+':10'
                time_stamp5=data+str(time)+':20'
                time_stamp6=data+str(time)+':30'
                time_stamp7=data+str(time)+':50'
                time_stamp8=data+str(time+1)+':00'
                time_stamp9=data+str(time+1)+':10'
                time_stamp10=data+str(time+1)+':20'
                time_stamp11=data+str(time+1)+':30'
                time_stamp12=data+str(time+1)+':40'
                median_list=[float(time_dict[time_stamp]),float(time_dict[time_stamp3]),float(time_dict[time_stamp4]),
                         float(time_dict[time_stamp5]),float(time_dict[time_stamp6]),float(time_dict[time_stamp7]),
                         float(time_dict[time_stamp8]),float(time_dict[time_stamp9]),float(time_dict[time_stamp10])]
                dat=median(median_list)
                if time<10:
                    pre="2016-09-"+data+" 0"+str(time)+':00'
                else:
                    pre="2016-09-"+data+" "+str(time)+':00'
                save_l=[dat,pre]
                save_list.append(save_l)
            if time_stamp==data+str(time)+':50':
                time_stamp1=data+str(time-1)+':50'
                time_stamp2=data+str(time)+':00'
                time_stamp3=data+str(time)+':10'
                time_stamp4=data+str(time)+':20'
                time_stamp5=data+str(time)+':30'
                time_stamp6=data+str(time)+':40'
                time_stamp7=data+str(time+1)+':00'
                time_stamp8=data+str(time+1)+':10'
                time_stamp9=data+str(time+1)+':20'
                time_stamp10=data+str(time+1)+':30'
                time_stamp11=data+str(time+1)+':40'
                time_stamp12=data+str(time+1)+':50'
                median_list=[float(time_dict[time_stamp]),float(time_dict[time_stamp3]),float(time_dict[time_stamp4]),
                         float(time_dict[time_stamp5]),float(time_dict[time_stamp6]),float(time_dict[time_stamp7]),
                         float(time_dict[time_stamp8]),float(time_dict[time_stamp9]),float(time_dict[time_stamp10])]
                dat=median(median_list)
                if time<10:
                    pre="2016-09-"+data+" 0"+str(time)+':00'
                else:
                    pre="2016-09-"+data+" "+str(time)+':00'
                save_l=[dat,pre]
                save_list.append(save_l)
        # f.write('%d,%s\n'%(time_dict[time_stamp],time_stamp))
    f = open("../merge_10_meidian/"+file_name, "wb")
    write = csv.writer(f)
    write.writerow(["passengerCount", "timeStamp"])
    write.writerows(save_list)
    f.close()