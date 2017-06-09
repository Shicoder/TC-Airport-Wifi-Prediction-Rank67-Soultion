import csv
import os
import cPickle
direction = "../merge_10/"
file_list = os.listdir(direction)
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
val_24= cPickle.load(open("../24_val.pkl","rb"))
sum=0
rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_win_5day(19-24).csv",'rb'))
rows_f.next()
cum=0
for row in rows_f:
    # print str(row[1])+":"+str(row[2])
    key = str(row[1])+":"+row[2].split("-")[0]+"-"+\
        row[2].split("-")[1]+"-24-"+row[2].split("-")[3]+\
        "-"+row[2].split("-")[4]
    if val_24.has_key(key):
        cum+=1
        sum+=(float(val_24[key])-float(row[0]))**2
        print cum
print sum
# for file_name in file_list:
#     file_path = direction+file_name
#     rows = csv.reader(open(file_path,'rb'))
#     rows.next()
#     for row in rows:
#         if row[1]=="2016-09-24 15:00":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-15-0':
#                     sum+=(row[0]-row_f[0])**2
#                     print sum
#         if row[1]=="2016-09-24 15:10":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-15-1':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 15:20":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-15-2':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 15:30":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-15-3':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 15:40":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-15-4':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 15:50":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-15-5':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 16:00":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-16-0':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 16:10":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-16-1':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 16:20":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-16-2':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 16:30":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-16-3':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 16:40":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-16-4':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 16:50":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-16-5':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 17:00":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-17-0':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 17:10":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-17-1':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 17:20":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-17-2':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 17:30":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-17-3':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 17:40":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-17-4':
#                     sum+=(row[0]-row_f[0])**2
#         if row[1]=="2016-09-24 17:50":
#             rows_f = csv.reader(open("../submit/airport_gz_passenger_predict_simple_dot_mean.csv",'rb'))
#             rows_f.next()
#
#             for row_f in rows_f:
#                 if row_f[1]==wifi_name_dict[int(file_name.split(".")[0])] and\
#                         row_f[2]=='2016-09-24-17:5':
#                     sum+=(row[0]-row_f[0])**2
print sum


