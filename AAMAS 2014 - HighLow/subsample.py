import os
import fnmatch
import csv
import math 
vals = os.listdir ('.')

dataDict = dict()
YVals = list()
YValsDone = 0

for val in vals:
        if val == 'subsample.py' or val == 'best':
                continue
        f = open(val, "r").readlines()
        rhs = val.split('-')[2]  
        cluster = rhs.split('.')[0]
        reader = csv.reader(f)
        dataList = list()
        XErr = list()
        for row in reader:
                print(row)
                ele = row[len(row)-2]
                eleVal = int(ele.split('.')[0])
                dataList.append(eleVal)
                if YValsDone == 0:
                        YVals.append(row[len(row)-3])
                XErr.append(row[len(row)-1])

        print(dataList)
        print(YVals)
        YValsDone = 1

        jumps = (len(dataList)-1)/10.0
        
        avg = 0
        subsampledDataX = list()
        subsampledDataY = list()
        j = 0
        for i in range(0,len(dataList)):
                XVal = dataList[i]
                avg = (XVal + j * avg)/(j + 1.0)
                j = j + 1
                if(int(i % jumps) == 0):
                        subsampledDataX.append(avg)
                        subsampledDataY.append(YVals[i])
                        avg = 0
                        j = 0
                        
        
        print(len(subsampledDataX))
        print(len(subsampledDataY))
        print(len(XErr))
        output = open('Learning-D-' + cluster + '-subsampled.csv', "w")
        for ele in range(0, len(subsampledDataX)):
                output.write(str(subsampledDataY[ele]) + ','+ str(subsampledDataX[ele]) + ',' + str(XErr[ele]) + '\n')
        output.close()
