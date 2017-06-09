__author__ = 'shi'
# -*- encoding:utf-8 -*-
import cPickle
key_list = []
value_list = []
mydisc = cPickle.load(open("../wifi_name_dict.pkl","rb"))
for key,value in mydisc.items():
    key_list.append(key)
    value_list.append(value)

get_value = "T1-1D-4<T1-1-03>"
if get_value in value_list:
    get_value_index = value_list.index(get_value)
    print "key:" ,key_list[get_value_index]
else:
    print "no%s" %get_value