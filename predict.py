import pandas as pd
import xgboost as xgb
from sklearn import metrics
from sklearn.linear_model import LinearRegression

train = pd.read_csv(r"C:\Users\28634\Desktop\train.csv", index_col='Date')
test = pd.read_csv(r"C:\Users\28634\Desktop\test.csv", index_col='Date')
# train = pd.read_csv(r"C:\Users\28634\Desktop\train.csv")
# test = pd.read_csv(r"C:\Users\28634\Desktop\test.csv")

# dtrain = xgb.DMatrix(train, label=train['Closing price'])
# dtest = xgb.DMatrix(test)

xgb_model = xgb.XGBRegressor(max_depth=8, learning_rate=0.1, booster='gbtree', maxDepth=3)
X = train
X.drop(columns=['Closing_price'], inplace=True)
Y = train.iloc[:, -1]
model = xgb_model.fit(X, Y)
result = model.predict(test)
a=1

# clf = LinearRegression(n_jobs=-1)
# clf.fit(X, Y)
# pred = clf.predict(test)


