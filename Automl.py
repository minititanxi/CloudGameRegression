import autokeras as ak
import pandas as pd
from sklearn import metrics, preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.neural_network import MLPRegressor  # 多层线性回归
from sklearn.preprocessing import StandardScaler
train = pd.read_csv('train.csv')  # 训练数据train
result=pd.DataFrame(train)
print(result.info())
X_train = train.values[0:,1:-1]#取样本数据，所有行，除了0,和最后3列的所有列 现在第0列是游戏名
y_train = train.values[0:,-1]

test = pd.read_csv('test.csv')  # 训练数据test
X_test = test.values[0:,1:-1]#取样本数据，所有行，除了0,和最后1列的所有列 现在第0列是游戏名
y_test = test.values[0:,-1]
min_max_scaler = preprocessing.MinMaxScaler()
X_train = min_max_scaler.fit_transform(X_train)
X_test = min_max_scaler.fit_transform(X_test)
clf = ak.ImageClassifier()
clf.fit(x_train, y_train)
results = clf.predict(x_test)