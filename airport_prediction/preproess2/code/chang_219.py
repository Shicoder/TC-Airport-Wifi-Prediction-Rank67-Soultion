__author__ = 'hp'
import csv
rows = csv.reader(open("../merge_10/232.csv",'rb'))
rows.next()
dataall=[]
for row in rows:
    data1=row[1].split("/")[0]
    data2=row[1].split("/")[1]
    data3=row[1].split("/")[2].split(" ")[0]
    data4 =row[1].split("/")[2].split(" ")[1]
    time = data1+"-0"+data2+"-"+data3
    if int(data4.split(":")[0])<10:
        time=time+" 0"+data4
    else:
        time=time+" "+data4
    data = [row[0],time]
    dataall.append(data)
f = open("../gbdt_feat/232.csv", "wb")
write = csv.writer(f)
write.writerow(["passengerCount", "timeStamp"])
write.writerows(dataall)
f.close()