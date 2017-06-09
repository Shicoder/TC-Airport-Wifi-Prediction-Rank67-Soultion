import csv
wifi_api_files = file('../data/15.csv', 'rb')
# wifi_api_files = file('../test/reslut10_4.csv', 'rb')
# wifi_api_files = file('../test/airport_gz_passenger_predict_qianhou1_10-14.csv', 'rb')
rows = csv.reader(wifi_api_files)
rows.next()
print "splitting...."
for row in rows:
    if float(row[0])>20:
        print row[1]

