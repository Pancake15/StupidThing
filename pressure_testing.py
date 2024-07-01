import numpy as np
import pandas as pd
import matplotlib as mpl
import sklearn

from sklearn.linear_model import LinearRegression

def secret_code():
    z = int(np.__version__.split('.')[0]) + 10*int(np.__version__.split('.')[0]) + 100*int(mpl.__version__.split('.')[0]) + 1000*int(sklearn.__version__.split('.')[0])
    X = np.loadtxt("X.txt", delimiter=",")
    lr = LinearRegression()
    lr.fit(X[:,:2],X[:,2])
    return round(z*lr.coef_.round(2)[0]*lr.coef_.round(2)[1])