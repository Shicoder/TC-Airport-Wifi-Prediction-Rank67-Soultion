import csv
import cPickle
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
rows = csv.reader(open("../submit/reslut_xgboost_10_21_2adddengjikou.csv",'rb'))
w_lists=[]
rows.next()
for row in rows:
    name = wifi_name_dict[int(row[1])]
    pre_date="2016-09-25-"
    slice10h=15+(int(row[2])-1)/6
    slice10m=(int(row[2])-1)%6
    pre_data=pre_date+str(slice10h)+"-"+str(slice10m)
    w_list = [row[0],name,pre_data]
    w_lists.append(w_list)
f = open("../submit/predict_xgboost_weight1_adddengjikou.csv", "wb")
write = csv.writer(f)
write.writerow(["passengercount", "WIFIAPTag","slice10min"])
write.writerows(w_lists)
f.close()