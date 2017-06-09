__author__ = 'shi'
import cPickle
wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
count =0
print
for i in range(749):
    if wifi_name_dict[i+1][0:2] !='E1' and  wifi_name_dict[i+1][0:2] !='E2'and wifi_name_dict[i+1][0:2] !='E3'\
        and wifi_name_dict[i+1][0:2] !='EC'and wifi_name_dict[i+1][0:2] !='T1'and wifi_name_dict[i+1][0:2] !='W1'\
        and wifi_name_dict[i+1][0:2] !='W2'and wifi_name_dict[i+1][0:2] !='W3' and wifi_name_dict[i+1][0:2] !='WC':
        count +=1
        print wifi_name_dict[i+1]
print count