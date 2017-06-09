    # from sklearn.ensemble import GradientBoostingClassifier
    # model = GradientBoostingClassifier(n_estimators=200)
    # model.fit(train_x, train_y)
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
import pandas as pd
df = pd.read_csv("../gbdt_feat/features.csv",index_col="wifi_name")
data =
import csv
# data = np.loadtxt("output_res(1).txt")
# rows = csv.reader(open("../features.csv",'rb'))
# rows.next()
# for row in rows:
data = np.loadtxt(open("../gbdt_feat/features.csv","rb"),delimiter=",",skiprows=0)
lable = np.loadtxt("../gbdt_feat/lables.txt")
print "data.shape",data.shape
print "lables.shape",lable.shape
from sklearn.cross_validation import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data, lable, test_size = 0.3)
clf2=GradientBoostingClassifier(loss = 'deviance',n_estimators=1000,learning_rate=0.01,max_depth=20)
# clf2.fit(x_train,y_train)
clf2.fit(x_train, y_train)
# for m in range(len(model.feature_importances_)):
#     if model.feature_importances_[m]>0.05:
#         print "feature_importance",m,model.feature_importances_[m]
answer = clf2.predict(x_test)
print "predict_result:",np.mean( answer == y_test)