__author__ = 'shi'
# -*- encoding:utf-8 -*-
import cPickle
key_list = []
value_list = []
mydisc = cPickle.load(open("../wifi_name_dict.pkl","rb"))
print mydisc[88]
for key,value in mydisc.items():
    key_list.append(key)
    value_list.append(value)

get_value = "E3-3A<E3-3-25>"
if get_value in value_list:
    get_value_index = value_list.index(get_value)
    print "key:" ,key_list[get_value_index]
else:
    print "no%s" %get_value