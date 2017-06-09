
def LR_model(features, lables):
    print "start train"
    import numpy as np
    feat=np.array(features)
    # feat=feat.astype(np.float)
    la=np.array(lables)
    # la=la.astype(np.float)
    from sklearn.linear_model import LinearRegression
    clf2 = LinearRegression(normalize=True)
    print "start fitting"
    clf2.fit(feat, la)
    print clf2.intercept_
    print clf2.coef_
    return clf2