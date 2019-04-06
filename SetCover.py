import random

import pandas as pd
from sklearn.externals import joblib
import numpy as np

def backtrack(result, model, combination, maxNumofColocation,performanceCounter):#回溯减枝生成可行满足延迟要求的游戏组合
    if(len(combination)==0):
        for i in range(30):
            if (len(combination) > maxNumofColocation - 1):
                return
            combination.append(i)
            backtrack(result, model, combination, maxNumofColocation, performanceCounter)
            combination.pop()
    if (isSatisfying(performanceCounter, model, combination, maxNumofColocation)):
        result.append(np.array(combination))
    else:
        return
    for i in range(30):
        if (len(combination) > maxNumofColocation - 1):
            return
        combination.append(i)
        backtrack(result, model, combination, maxNumofColocation, performanceCounter)
        combination.pop()


def isSatisfying(performanceCounter, model, combination, maxNumofColocation):#判断某一个组合是否满足延迟QOS

    data1 = []
    data2 = []
    if (len(combination) == 0):
        return 0
    for i in range(len(combination)):
        for j in range(1, 12):
            data2.append(performanceCounter[combination[i]][j])
        temp = combination.pop(0)
        for k in range(len(combination)):
            for j in range(1, 12):
                data2.append(performanceCounter[combination[k]][j])
        combination.append(temp)
        for j in range(6*11-len(combination)*11):
            data2.append(0)
        data1.append(np.array(data2))
        data2.clear()
    y_test = model.predict(np.array(data1))
    for i in range(len(y_test)):
        y_test[i] = performanceCounter[combination[i]][11] * (1-y_test[i])
    for i in range(len(y_test)):
        # print(1000/y_test[i])
        if (1000 / y_test[i] > 15):
            return 0
    return 1

def generateRequestData(requestList,numOfRequest):#生成请求数据
    request=[]#游戏编号和传输延迟的二元组
    for i in range(numOfRequest):
        gameNumber = random.randint(1,100)
        playerDelay = random.randint(30, 100)
        request.append(gameNumber)
        request.append(playerDelay)
        requestList.append(np.array(request))
        request.clear()


df1 = pd.DataFrame(pd.read_csv('PerformanceCounter.csv'))
print(df1.values)  # Game Counter 二维数组
performanceCounter=df1.values
model = joblib.load('RFmodel')
result=[]
combination=[]
maxNumofColocation=4
backtrack(result, model, combination, maxNumofColocation,performanceCounter)
print("结果总数：")
print(len(result))
# for i in range(len(result)):
#     if(len(result[i])==1):
#         for j in range(len(result[i])):
#             print(result[i][j])
#         print('\n')

