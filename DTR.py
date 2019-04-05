from sklearn.tree import DecisionTreeRegressor
import pandas as pd
from sklearn import metrics
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
train = pd.read_csv('train.csv')  # 训练数据train
X_train = train.values[0:,1:-1]#取样本数据，所有行，除了0,和最后3列的所有列 现在第0列是游戏名
y_train = train.values[0:,-1]

test = pd.read_csv('test.csv')  # 训练数据test
X_test = test.values[0:,1:-1]#取样本数据，所有行，除了0,和最后1列的所有列 现在第0列是游戏名
y_test = test.values[0:,-1]

model = DecisionTreeRegressor(max_depth=100)
model.fit(X_train, y_train)
y_predict=model.predict(X_test)
print(y_test)
print(y_predict)
print(mean_squared_error(y_train,model.predict(X_train)))
print(mean_squared_error(y_test,y_predict))
sum=0.0
for i in range(146):
    sum = sum + (1-y_predict[i])/(1-y_test[i])
sum=sum/146
sum=sum-1
print(sum)

print(sum)


