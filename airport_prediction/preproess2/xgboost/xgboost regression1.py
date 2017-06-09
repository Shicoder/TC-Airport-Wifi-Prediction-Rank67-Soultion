#Import libraries:
import pandas as pd
import numpy as np
import xgboost as xgb
import csv
from xgboost.sklearn import XGBRegressor
import cPickle
from sklearn import cross_validation, metrics   #Additional     scklearn functions
from sklearn.grid_search import GridSearchCV   #Perforing grid search

import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
train_data = np.loadtxt(open("../gbdt_feat/xgboost_feat_train_wight_nomean.csv","rb"),delimiter=",",skiprows=0)
# train_data = pd.read_csv("../gbdt_feat/xgboost_feat_train_wight_mean_add_quyurenshu.csv",sep=',',names=range(31))
train_data=np.array(train_data)
print  train_data.shape
train_data=np.asarray(train_data, dtype=np.float64)
train_target = np.loadtxt(open("../gbdt_feat/xgboost_train_lable_weight_mean.csv","rb"),delimiter=",",skiprows=0)
# train_target = pd.read_csv("../train/xgboost_train_lable_weight_mean.csv",sep=',',names=range(1))
print train_target
train_target =np.array(train_target)
print  train_target.shape
train_target=np.asarray(train_target, dtype=np.float64)

train_data=np.asarray(train_data, dtype=np.float64)
#########################################################
test_data = np.loadtxt(open("../gbdt_feat/xgboost_feat_train_wight_nomean.csv","rb"),delimiter=",",skiprows=0)

# test_data = pd.read_csv("../gbdt_feat/xgboost_target_addquyurenshu.csv",sep=',',names=range(31))
test_data =np.array(test_data)
test_data=np.asarray(test_data, dtype=np.float64)
print test_data
print  test_data.shape
def daochu(pred):
    listpred=[]
    f = open('../gbdt_feat/xgboost_target_weight_nomean.csv')
    num=0
    rows = csv.reader(f)
    for row in rows:
        wifi_name_dict = cPickle.load(open("../wifi_name_dict.pkl","rb"))
        name = wifi_name_dict[int(float(row[1]))]
        pre_date="2016-09-25-"
        slice10h=15+(int(float(row[2]))-1)/6
        slice10m=(int(float(row[2]))-1)%6
        pre_data=pre_date+str(slice10h)+"-"+str(slice10m)
        listpred.append([list(pred)[num],name, pre_data])
        num=num+1
    result = pd.DataFrame(listpred,columns=['pass','name','time'])
    result.to_csv("../train/reslut_xgboost_10_21_weight_nomean.csv", index=False)
def get_xgb_feat_importances(clf):

    if isinstance(clf, xgb.XGBModel):
        # clf has been created by calling
        # xgb.XGBClassifier.fit() or xgb.XGBRegressor().fit()
        fscore = clf.booster().get_fscore()
    else:
        # clf has been created by calling xgb.train.
        # Thus, clf is an instance of xgb.Booster.
        fscore = clf.get_fscore()

    feat_importances = []
    for ft, score in fscore.iteritems():
        feat_importances.append({'Feature': ft, 'Importance': score})
    feat_importances = pd.DataFrame(feat_importances)
    feat_importances = feat_importances.sort_values(
        by='Importance', ascending=False).reset_index(drop=True)
    # Divide the importances by the sum of all importances
    # to get relative importances. By using relative importances
    # the sum of all importances will equal to 1, i.e.,
    # np.sum(feat_importances['importance']) == 1
    feat_importances['Importance'] /= feat_importances['Importance'].sum()
    # Print the most important features and their importances
    print feat_importances
    return feat_importances
def modelfit(alg, train_data, train_target,test_data,useTrainCV=True, cv_folds=5, early_stopping_rounds=50):
    if useTrainCV:
        print  'jiachayanzheng'
        xgb_param = alg.get_xgb_params()
        xgtrain = xgb.DMatrix(train_data, label=train_target)
        cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=alg.get_params()['n_estimators'], nfold=cv_folds, early_stopping_rounds=early_stopping_rounds)
        alg.set_params(n_estimators=cvresult.shape[0])

    #Fit the algorithm on the data
    print  'kaishixunlian'
    alg.fit(train_data, train_target)
    print  'kaishiyuce'
    dtrain_predictions = alg.predict(test_data)
    daochu(dtrain_predictions)
    print  'Feature Importance'
    get_xgb_feat_importances(alg)
    # Print Feature Importance:
    # feat_imp = pd.Series(get_xgb_feat_importances(alg)(1)).sort_values(ascending=False)
    # feat_imp.plot(kind='bar', title='Feature Importances')
    # plt.ylabel('Feature Importance Score')
    # plt.show()
    # get_xgb_feat_importances(alg)

xgb1 = XGBRegressor(
learning_rate =0.01,
 n_estimators=1000,
 max_depth=6,
 min_child_weight=6,
 gamma=0,
 subsample=0.8,
 colsample_bytree=0.8,
 reg_alpha=0.005,
 objective= 'reg:linear',
 nthread=14,
 scale_pos_weight=3,
 seed=2016
 )
modelfit(xgb1, train_data, train_target,test_data)
