import pandas as pd
from sklearn import metrics, preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
train = pd.read_csv('train.csv')  # 训练数据train
result=pd.DataFrame(train)
print(result.info())
X_train = train.values[0:,1:-1]#取样本数据，所有行，除了0,和最后3列的所有列 现在第0列是游戏名
y_train = train.values[0:,-1]

test = pd.read_csv('test.csv')  # 训练数据test
X_test = test.values[0:,1:-1]#取样本数据，所有行，除了0,和最后1列的所有列 现在第0列是游戏名
y_test = test.values[0:,-1]

model = GradientBoostingRegressor(n_estimators=80,max_depth=5,learning_rate=0.038,min_samples_split=150)
model.fit(X_train, y_train)
print(model.feature_importances_ )
y_predict=model.predict(X_test)
print(y_test)
print(y_predict)
# param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(100,801,200),}
# gsearch2 = GridSearchCV(model, param_test2)
# gsearch2.fit(X_train,y_train)
# print(gsearch2.best_params_)
sum=0.0
print(X_test.shape[0])
for i in range(X_test.shape[0]):
    if(y_predict[i]<0):
        y_predict[i]=0
    sum=sum+abs(y_test[i]-y_predict[i])/(1-y_test[i])
    # sum = sum + abs(y_test[i] - y_predict[i])
sum=sum/X_test.shape[0]
# sum=sum-1
print(sum)







