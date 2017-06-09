import pandas as pd
import cPickle
import shutil
series_list={}
num=0
list2=[]
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
for i in range(749):
    df = pd.read_csv("../merge_10/"+str(i+1)+".csv")
    # df = pd.read_csv("../merge_10_check/checkin.csv",index_col="timeStamp")
    df.index = pd.to_datetime(df.index)
    ts = df['passengerCount']
    # print df1.describe()
    # test_stationarity.draw_ts1(ts1)
    if  ts.std()>1 :
        num+=1
        test=[i+1,wifi_name_dict[i+1],ts.mean()]
        list2.append(test)
        print i+1,wifi_name_dict[i+1],ts.mean()
        shutil.copyfile("../merge_10/"+str(i+1)+".csv","../stddayu1/"+str(i+1)+".csv")
print "sum:",num
import csv
f = open("mean.csv", "wb")
write = csv.writer(f)
write.writerows(list2)
f.close()