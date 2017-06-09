import pandas as pd
import cPickle
wifi_name_dict = cPickle.load(open("../all_win_5_meidian.pkl","rb"))
print wifi_name_dict["EC-1I<EC-1I-13>-1"]