import csv
import cPickle
rows = csv.reader(open("../ori_data/xgboost_feat_quyurenshu.csv",'rb'))
rows.next()
pjf_feat_dict={}
for row in rows:
    key = row[1]+"-"+row[0].split("-")[2]+"-"+row[2]

    pjf_feat_dict[key]=row[3:]
f = open("../pjf_feat_train_quyurenshu.pkl",'wb')
cPickle.dump(pjf_feat_dict,f,-1)
f.close()
# rows = csv.reader(open("../ori_data/gbdt_feat_target(1).csv",'rb'))
# rows.next()
# pjf_feat_dict1={}
# for row in rows:
#     key = row[1]+"-"+row[0].split("-")[2]+"-"+row[2]
#     print key
#     pjf_feat_dict1[key]=row[3:]
# f = open("../pjf_feat_predict(1).pkl",'wb')
# cPickle.dump(pjf_feat_dict1,f,-1)
# f.close()