import csv


import pandas as pd
from numpy import NaN
# -*- coding: utf-8 -*-

df1 = pd.DataFrame(pd.read_csv('PerformanceCounter.csv'))
print (df1.info())
# print(df1.isnull())
print(df1.values)#Game Counter 二维数组

df2 = pd.DataFrame(pd.read_csv('Colocation.csv'))
# print(df2.info)
# print(df2.isnull())
# print(df2.values)
print(df2.values[0][3])
if df2.values[0][3]!=df2.values[0][3]:
    print("hehe")
print(type(df2.values[0]))
print(df1.values[int(df2.values[0][0]) - 1][0])
out = open('TestData.csv','w', newline='')
csv_write = csv.writer(out,dialect='excel')
for i in range(565):
    if df2.values[i][2] != df2.values[i][2]:#2_colocation
        data1=[]
        data1.append(df2.values[i][0])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][0])-1][j])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][1])-1][j])
        data1.append(2)
        data1.append((df1.values[int(df2.values[i][0])-1][11]-df2.values[i][4])/df1.values[int(df2.values[i][0])-1][11])
        csv_write.writerow(data1)
        data1.clear()
        data1.append(df2.values[i][1])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][1]) - 1][j])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][0])-1][j])
        data1.append(2)
        data1.append(
            (df1.values[int(df2.values[i][1]) - 1][11] - df2.values[i][5]) / df1.values[int(df2.values[i][1]) - 1][11])
        csv_write.writerow(data1)
        data1.clear()

    elif df2.values[i][3] != df2.values[i][3]:#3_colocation

        data1 = []
        data1.append(df2.values[i][0])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][0]) - 1][j])
        for j in range(1,11):
            data1.append((df1.values[int(df2.values[i][1]) - 1][j]+df1.values[int(df2.values[i][2]) - 1][j])/2)
        data1.append(3)
        data1.append(
            (df1.values[int(df2.values[i][0]) - 1][11] - df2.values[i][4]) / df1.values[int(df2.values[i][0]) - 1][11])
        csv_write.writerow(data1)
        data1.clear()
        data1.append(df2.values[i][1])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][1]) - 1][j])
        for j in range(1,11):
            data1.append((df1.values[int(df2.values[i][0]) - 1][j]+df1.values[int(df2.values[i][2]) - 1][j])/2)
        data1.append(3)
        data1.append(
            (df1.values[int(df2.values[i][1]) - 1][11] - df2.values[i][5]) / df1.values[int(df2.values[i][1]) - 1][11])

        csv_write.writerow(data1)
        data1.clear()
        data1.append(df2.values[i][2])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][2]) - 1][j])
        for j in range(1,11):
            data1.append((df1.values[int(df2.values[i][0]) - 1][j]+df1.values[int(df2.values[i][1]) - 1][j])/2)
        data1.append(3)
        data1.append(
            (df1.values[int(df2.values[i][2]) - 1][11] - df2.values[i][6]) / df1.values[int(df2.values[i][2]) - 1][11])

        csv_write.writerow(data1)
        data1.clear()

    else:#4_colocation

        data1 = []
        data1.append(df2.values[i][0])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][0] )- 1][j])
        for j in range(1,11):
            data1.append((df1.values[int(df2.values[i][1]) - 1][j]+df1.values[int(df2.values[i][2]) - 1][j]+df1.values[int(df2.values[i][3] )- 1][j])/3)
        data1.append(4)
        data1.append(
            (df1.values[int(df2.values[i][0]) - 1][11] - df2.values[i][4]) / df1.values[int(df2.values[i][0]) - 1][11])

        csv_write.writerow(data1)
        data1.clear()

        data1 = []
        data1.append(df2.values[i][1])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][1]) - 1][j])
        for j in range(1,11):
            data1.append((df1.values[int(df2.values[i][0]) - 1][j]+df1.values[int(df2.values[i][2] )- 1][j]+df1.values[int(df2.values[i][3]) - 1][j])/3)
        data1.append(4)
        data1.append(
            (df1.values[int(df2.values[i][1]) - 1][11] - df2.values[i][5]) / df1.values[int(df2.values[i][1]) - 1][11])
        csv_write.writerow(data1)
        data1.clear()

        data1 = []
        data1.append(df2.values[i][2])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][2]) - 1][j])
        for j in range(1,11):
            data1.append((df1.values[int(df2.values[i][0]) - 1][j]+df1.values[int(df2.values[i][1]) - 1][j]+df1.values[int(df2.values[i][3]) - 1][j])/3)
        data1.append(4)
        data1.append(
            (df1.values[int(df2.values[i][2]) - 1][11] - df2.values[i][6]) / df1.values[int(df2.values[i][2]) - 1][11])

        csv_write.writerow(data1)
        data1.clear()

        data1 = []
        data1.append(df2.values[i][3])
        for j in range(1,11):
            data1.append(df1.values[int(df2.values[i][3]) - 1][j])
        for j in range(1,11):
            data1.append((df1.values[int(df2.values[i][0]) - 1][j]+df1.values[int(df2.values[i][1]) - 1][j]+df1.values[int(df2.values[i][2]) - 1][j])/3)
        data1.append(4)
        data1.append(
            (df1.values[int(df2.values[i][3]) - 1][11] - df2.values[i][7]) / df1.values[int(df2.values[i][3]) - 1][11])
        csv_write.writerow(data1)
        data1.clear()
out.close()