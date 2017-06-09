import cPickle
import os
import csv
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
direction = "../merge_10_meidian/"
file_list = os.listdir(direction)
for file_name in file_list:
    file_path = direction+file_name
    rows = csv.reader(open(file_path,'rb'))
    rows.next()
    f = open("../merge_10_meidian_1/"+file_name, "wb")
    write = csv.writer(f)
    write.writerow(["passengerCount", "timeStamp"])
    for row in rows:
        nrow=[row[1],row[0][:-3]]
        write.writerow(nrow)
    f.close()