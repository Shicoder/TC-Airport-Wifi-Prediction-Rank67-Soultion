__author__ = 'shi'
import csv
import cPickle
import os
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
filetoread=open('../submit/airport_gz_passenger_predict.csv','r')
reader = csv.reader(filetoread)
direction = "../test_data/"
file_list = os.listdir(direction)
for file_name in file_list:
    file_path = direction + file_name
    filetowrite=open(file_path,'ab')
    num=int(file_name.split(".")[0])
    name=wifi_name_dict[num]
    writer=csv.writer(filetowrite)
    for line in reader:
        if line[1]==name:
            u1, u2, u3, u4, u5 = line[2].split('-')
            gang = '-'
            maohao = ':'
            u1 += gang
            u1 += u2
            u1 += gang
            u1 += u3
            u5 += "0"
            u4 += maohao
            u4 += u5
            line_1=u1+' '+u4
            data=[line[0],line_1]
            writer.writerow(data)
    filetowrite.close()
filetoread.close()
