import os
import csv
import cPickle
direction = "../win_5_day(19-24)/"
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
file_list = os.listdir(direction)
all_list=[]
for file_name in file_list:
    if file_name.split(".")[0]=='53' or file_name.split(".")[0]=='90' \
       or file_name.split(".")[0]=='219' or file_name.split(".")[0]=='232'\
        or file_name.split(".")[0]=='374'or file_name.split(".")[0]=='608'\
        or file_name.split(".")[0]=='84'or file_name.split(".")[0]=='160'\
        or file_name.split(".")[0]=='292'or file_name.split(".")[0]=='347'\
        or file_name.split(".")[0]=='385'or file_name.split(".")[0]=='471'\
        or file_name.split(".")[0]=='499'or file_name.split(".")[0]=='596':
            file_path = direction+file_name
            rows = csv.reader(open(file_path,'rb'))
            rows.next()
            for row in rows:
                pre_data="2016-09-25-"
                data1=row[1].split(":")[0]
                data2=row[1].split(":")[1][0]
                pre_data=pre_data+data1+"-"+data2
                if file_name.split(".")[0]=='499'or file_name.split(".")[0]=='347'or\
                    file_name.split(".")[0]=='471':
                    date=float(row[0])*1.2
                    name=wifi_name_dict[int(file_name.split(".")[0])]
                    all_list.append([date,name,pre_data])
                else:
                    date=float(row[0])
                    name=wifi_name_dict[int(file_name.split(".")[0])]
                    all_list.append([date,name,pre_data])
f = open("../gbdt_feat/yichangshuju_result.csv", "wb")
write = csv.writer(f)
write.writerow(["passengerCount", "WIFIAPTag","slice10min"])
write.writerows(all_list)
f.close()