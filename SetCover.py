import pandas as pd
from sklearn.externals import joblib
def backtrack(result,model,combination,maxNumofColocation):
    if(isSatisfying(model,combination) and len(combination)<=maxNumofColocation):
        result.append(combination)
    else:
        for i in range(100):
            if(len(combination)>maxNumofColocation-1):
                return
            combination.append(i)
            backtrack(result, model, combination, maxNumofColocation)
            combination.pop()



def isSatisfying(performanceCounter,model,combination):
    data1=[]
    data2=[]
    for i in range(len(combination)):
        for j in range(1,12):
            data2.append(performanceCounter[i-1][j])
        temp=combination.pop(0)
        for k in range(len(combination)):
            for j in range(1, 12):
                data2.append(performanceCounter[k - 1][j])
        combination.append(temp)
        data1.append(data2)
        data2.clear()
    y_test=model.predict(data2)
    for i in range(len(y_test)):
        y_test[i]=performanceCounter[combination[i] - 1][11]*y_test[i]
    for i in range(len(y_test)):
        if(1/y_test[i]>100):
            return 0
    return y_test





df1 = pd.DataFrame(pd.read_csv('PerformanceCounter.csv'))
print(df1.values)#Game Counter 二维数组
clf=joblib.load('RFmodel')





