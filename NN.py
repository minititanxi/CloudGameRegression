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

model = MLPRegressor(
    hidden_layer_sizes=(8,4,2), max_iter=100000, activation='relu', solver='adam', alpha=0.00001, batch_size='auto',
    learning_rate='constant', learning_rate_init=0.000005, power_t=0.5, shuffle=True,
    random_state=1, tol=0.0001, verbose=False, warm_start=False, momentum=0.9, nesterovs_momentum=True,
    early_stopping=True,beta_1=0.9, beta_2=0.999, epsilon=1e-08)

model.fit(X_train, y_train)

y_predict=model.predict(X_test)
print(y_test)
print(y_predict)
# param_test2 = {'max_depth':range(3,14,2), 'min_samples_split':range(100,801,200),}
# gsearch2 = GridSearchCV(model, param_test2)
# gsearch2.fit(X_train,y_train)
# print(gsearch2.best_params_)
sum=0.0
for i in range(X_test.shape[0]):
    if(y_predict[i]<0):
        y_predict[i]=0
    sum=sum+abs(y_test[i]-y_predict[i])/(1-y_test[i])
sum=sum/X_test.shape[0]
# sum=sum-1
print(sum)







