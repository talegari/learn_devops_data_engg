import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.ensemble import RandomForestRegressor
import sklearn.datasets as datasets
import joblib

boston_raw = datasets.load_boston()
boston_X   = boston_raw.data
boston_Y   = boston_raw.target

regressor = RandomForestRegressor()
regressor

regressor.fit(boston_X, boston_Y)

predictions = regressor.predict(boston_X)
predictions[:10]
boston_Y[0:10]

joblib.dump(
  regressor
  , "/media/sf_srikanthk/code/learn_devops_data_engg/rf_regressor_boston.pkl"
  )
