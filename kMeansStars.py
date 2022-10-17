#python3 kMeansStars.py 

import csv
import math
import random

inVector = []
cheVector = []
with open("star_data.csv") as file:
    c = 0
    for row in reader:
        if c!=0:
            #inVector.append((math.log(float(row[0])),math.log(float(row[1])),math.log(float(row[2])),float(row[3])))
            inVector.append((math.log(float(row[0])),math.log(float(row[1])),math.log(float(row[2])),float(row[3]),int(row[4])))
        c+=1
    inVector = inVector[1:]

def kmeans(k):
    dic0 = {}
    dic1 = {}
    for v in random.sample(inVector,k):
        dic0[v] = []
    while(True):
        for v1 in inVector:
            dists = []
            for v2 in dic0.keys():
                i0 = (v1[0]-v2[0])**2
                i1 = (v1[1]-v2[1])**2
                i2 = (v1[2]-v2[2])**2
                i3 = (v1[3]-v2[3])**2
                dists.append((i0+i1+i2+i3,v2))
            dic0[min(dists)[1]].append(v1)
        for k in dic0.keys():
            temp = dic0[k]
            temp0 = [x[0] for x in temp]
            temp1 = [x[1] for x in temp]
            temp2 = [x[2] for x in temp]
            temp3 = [x[3] for x in temp]
            n0 = sum(temp0)/len(temp0)
            n1 = sum(temp1)/len(temp1)
            n2 = sum(temp2)/len(temp2)
            n3 = sum(temp3)/len(temp3)
            dic1[(n0,n1,n2,n3)] = []
        if(dic1.keys() == dic0.keys()):
            return dic0
        dic0 = dic1
        dic1 = {}
    
groupedDict = kmeans(6)

for m in groupedDict.keys():
    print("Mean: " + str(m))
    print("-------------------------")
    for s in groupedDict[m]:
        print("Star: " + str(s[0:3]))
        print("Type: " + str(s[4]))
    print()

