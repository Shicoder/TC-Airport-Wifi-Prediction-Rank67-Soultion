import os
import csv
import cPickle
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
direction = "../merge_10/"
file_list = os.listdir(direction)
cun_list=[]
for file_name in file_list:

    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    for row in rows:
            day = row[1].split(" ")[0][8:]
            time = row[1].split(" ")[1].split(":")[0]
            data=row[1].split(" ")[0]+"-"+time+"-"+row[1].split(" ")[1].split(":")[1][0]
            if day =='18' and (int(time)>=15 and int(time)<=17):
                list=[row[0],wifi_name_dict[int(file_name.split(".")[0])],data]
                cun_list.append(list)
f = open("../submit/offline_groundtruth_.csv", "wb")
write = csv.writer(f)
write.writerow(["passengerCount", "WIFIAPTag","slice10min"])
write.writerows(cun_list)
f.close()