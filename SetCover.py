import copy
import csv
import random

import pandas as pd
from sklearn.externals import joblib
import numpy as np

def backtrack(result, delayresult,model, combination, maxNumofColocation,performanceCounter):#回溯减枝生成可行满足延迟要求的游戏组合

    flag=isSatisfying(performanceCounter, model, combination, maxNumofColocation)[0]
    delay=isSatisfying(performanceCounter, model, combination, maxNumofColocation)[1]
    if (not flag and len(combination)>0):
        return
    elif(flag and len(combination)>0 ):
        print(len(result))
        print(combination)
        print(delay)
        result.append(np.array(combination))
        delayresult.append(np.array(delay))
    for i in range(100):
        if (len(combination) > maxNumofColocation - 1):
            return
        combination.append(i)
        backtrack(result, delayresult, model, combination, maxNumofColocation, performanceCounter)
        combination.pop()


def isSatisfying(performanceCounter, model, combination, maxNumofColocation):#判断某一个组合是否满足延迟QOS
    if (len(combination) == 0):
        return (0, 0)
    data1 = []
    data2 = []

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
        y_test[i]=1000/y_test[i]#延迟单位为ms
    for i in range(len(y_test)):
        # print(1000/y_test[i])
        if (y_test[i] >20):
            return (0,y_test)
    return (1,y_test)

def generateRequestData(requestData,numOfRequest):#生成请求数据
    request=[]#游戏编号和传输延迟的二元组
    for i in range(numOfRequest):
        gameNumber = random.randint(0,99)#游戏标号比实际值大1
        playerDelay = random.randint(30, 70)
        requestData[gameNumber].append(playerDelay)

def searchCombinationResultToFile(result,delayresult):#将回溯搜索结果输入文件，result为组合，delayresult为组合延迟
    data1 = []
    out1 = open('CombinationResult.csv', 'w', newline='')
    csv_write1 = csv.writer(out1, dialect='excel')
    for i in range(len(result)):
        data1=result[i]
        csv_write1.writerow(data1)
    out2 = open('CombinationDelayResult.csv', 'w', newline='')
    csv_write2 = csv.writer(out2, dialect='excel')
    for i in range(len(delayresult)):
        data1 = delayresult[i]
        csv_write2.writerow(data1)

def greedyAlgorithm(requestData,numOfRequest,Qos,server,serverdelay):#顶点覆盖贪心算法
    df1 = pd.DataFrame(pd.read_csv('CombinationResult.csv'))
    df2 = pd.DataFrame(pd.read_csv('CombinationDelayResult.csv'))
    print(df1.values)
    print(df2.values)
    combinationResult=np.array(df1.values)
    combinationDelay = np.array(df2.values)
    location=[]#记录每一个待选中请求的位置
    find=[]
    temp_server=[]
    temp_serverdelay=[]
    i=0
    while(numOfRequest>0):
        while(i<combinationResult.shape[0]):
            for j in range(len(combinationResult[i])):#列
                for k in range(len(requestData[combinationResult[i][j]])):#对应游戏请求个数
                    if(requestData[combinationResult[i][j]][k]+combinationDelay[i][j]<Qos):
                        location.append([combinationResult[i][j],k])
                        find.append(1)
                        break
                temp_server = combinationResult[i].tolist()
                print(temp_server)
                temp_serverdelay = combinationDelay[i].tolist()
                if(len(find)!=j+1):#搜索中发现后续游戏已无法满足条件，退出
                    location.clear()
                    find.clear()
                    i=i+1
                    break
            if(len(find)==len(combinationResult[i])):#满足条件
                server.append(copy.deepcopy(temp_server))
                for j in range(len(location)):
                    temp_serverdelay[j]=temp_serverdelay[j]+requestData[location[j][0]][k]
                serverdelay.append(copy.deepcopy(temp_serverdelay))
                temp_server.clear()
                temp_serverdelay.clear()
                find.clear()
                for j in range(len(location)):
                    requestData[location[j][0]].pop(location[j][1])
                    print(requestData)
                    numOfRequest=numOfRequest-1
                if(numOfRequest==0):
                    break
                location.clear()


df1 = pd.DataFrame(pd.read_csv('PerformanceCounter.csv'))
print(df1.values)  # Game Counter 二维数组
performanceCounter=df1.values
model = joblib.load('RFmodel')
result=[]
delayresult=[]
# searchCombinationResultToFile(result,delayresult)
combination=[]
maxNumofColocation=4
# backtrack(result,delayresult, model, combination, maxNumofColocation,performanceCounter)
print("结果总数：")
print(len(result))
print(len(delayresult))
# for i in range(len(result)):
#     if(len(result[i])==1):
#         for j in range(len(result[i])):
#             print(result[i][j])
Qos=100#延迟Qos
requestData={}
for i in range(100):
    requestData[i]=[]
requestData[1].append(10)
print(requestData)
# numOfRequest=1000
# # generateRequestData(requestData,numOfRequest)
# print(requestData)
numOfRequest=1
server=[]
serverdelay=[]
greedyAlgorithm(requestData,numOfRequest,Qos,server,serverdelay)
print(server)
print(serverdelay)
