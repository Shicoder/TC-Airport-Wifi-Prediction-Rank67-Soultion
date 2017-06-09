__author__ = 'shixiangfu'
import csv
import cPickle
wifi_api_files = file('../test/airport_gz_passenger_predict_qianhou1_10-14.csv', 'rb')
simple_day_hour1_2_mean=cPickle.load(open("../simple_day_1-2_hour_mean.pkl","rb"))
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
# wifi_api_files = file('../test/result10_14.csv', 'rb')
# wifi_api_files = file('../test/gbdt_result.csv', 'rb')
rows = csv.reader(wifi_api_files)
rows.next()
print "splitting...."
one_rows1=[]
count_rows=0
f = open("../submit/simple_2hour+mean.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
for row in rows:
    one_row = [float(row[0]),row[1],row[2]]
    simple_hour_name_pre =one_row[1]+":4-13"
    if row[1]==wifi_name_dict[348] or row[1]==wifi_name_dict[383] or row[1]==wifi_name_dict[520] or row[1]==wifi_name_dict[53] or\
           row[1]== wifi_name_dict[736]:
        data=float(row[0])
    else:
        data=0.7*simple_day_hour1_2_mean[simple_hour_name_pre]+0.3*one_row[0]
    write.writerow([data,one_row[1],one_row[2]])
f.close()