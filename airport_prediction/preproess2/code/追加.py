import os
import csv
import cPickle
direction = "../merge_10_add_predict/"
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
file_list = os.listdir(direction)

for file_name in file_list:

    name = wifi_name_dict[int(file_name.split(".")[0])]
    file_path = direction+file_name
    f=open(file_path,'ab')
    write = csv.writer(f)
    input_names=[]
    rows_f = csv.reader(open("../submit/predict_xgboost_best.csv",'rb'))
    rows_f.next()
    for row in rows_f:
        if row[1]==name:
            print file_name
            data = row[2].split("-")[0]+"-"+row[2].split("-")[1]+"-"+row[2].split("-")[2]\
            +" "+row[2].split("-")[3]+":"+row[2].split("-")[4]+"0"
            input_name = [row[0],data]
            input_names.append(input_name)
    write.writerows(input_names)
    f.close()

# for file_name in file_list:
#     data = row[2].split("-")[2]
#     file_path = direction+file_name
#     f=open(file_path,'rb')
#     write = csv.writer(f)
#     for row in rows: