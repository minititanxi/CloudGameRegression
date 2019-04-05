import pandas as pd
from sklearn import metrics, preprocessing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
train = pd.read_csv('train.csv')  # 训练数据train
result=pd.DataFrame(train)
print(result.info())
X_train = train.values[0:,1:-1]#取样本数据，所有行，除了0,和最后3列的所有列 现在第0列是游戏名
y_train = train.values[0:,-1]

test = pd.read_csv('test.csv')  # 训练数据test
X_test = test.values[0:,1:-1]#取样本数据，所有行，除了0,和最后1列的所有列 现在第0列是游戏名
y_test = test.values[0:,-1]
# param_test2 = {'n_estimators':range(20,200,10),'max_depth':range(3,20,2),'min_samples_split':range(2,20,2),
#                'min_samples_leaf':range(1,20,2)}
# gsearch = GridSearchCV(RandomForestRegressor(), param_test2,n_jobs=-1)
# gsearch.fit(X_train,y_train)
# # cv_result = pd.DataFrame.from_dict(gsearch.cv_results_)
# # with open('cv_result.csv','w') as f:
# #     cv_result.to_csv(f)
#
# print('The parameters of the best model are: ')
# print(gsearch.best_params_)
model = RandomForestRegressor(max_depth=19, n_estimators=40, min_samples_leaf=1,random_state=10,min_samples_split=2)
model.fit(X_train, y_train)
y_predict=model.predict(X_test)
print(y_test)
print(y_predict)
print(mean_squared_error(y_test,y_predict))
sum=0.0
for i in range(X_test.shape[0]):
    if(y_predict[i]<0):
        y_predict[i]=0
    print(abs(y_test[i]-y_predict[i]))
    sum=sum+abs(y_test[i]-y_predict[i])/(1-y_test[i])
    # sum=sum+abs(y_test[i]-y_predict[i])
sum=sum/X_test.shape[0]
# sum=sum-1
print(sum)







