import random
import urllib.request
import io
from PIL import Image
from urllib.request import Request, urlopen
import sys

URL = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
URL = 'data:image/jpeg;base64,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'
URL = sys.argv[1]
f = io.BytesIO(urllib.request.urlopen(URL).read())
img = Image.open(f) 

global K
K = int(sys.argv[2])

#part 1
def color27(img):
    pix = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            p = []
            for i in range(3):
                if pix[x,y][i] < 255//3: p.append(0)
                elif pix[x,y][i] < 255*2//3: p.append(255)
                else: p.append(127)
            pix[x,y] = (p[0],p[1],p[2])
    dic = {}
    temp = [0,127,255]
    for i in temp:
        for j in temp:
            for k in temp:
                dic[(i,j,k)] = []
    barsize = img.size[0]//len(dic.keys())
    imgbar = Image.new("RGB",(img.size[0],img.size[1]+barsize),0)
    pix2 = imgbar.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pix2[x,y] = pix[x,y]
    keys = list(dic.keys())
    means = [(round(temp[0]),round(temp[1]),round(temp[2])) for temp in keys]
    for x in range(img.size[0]):
        for y in range(img.size[1],imgbar.size[1]):
            pix2[x,y] = means[int(x/(img.size[0]/K))]
    imgbar.show()
    return imgbar,dic

def color8(img):
    pix = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            p = []
            for i in range(3):
                if pix[x,y][i] < 128: p.append(0)
                else: p.append(255)
            pix[x,y] = (p[0],p[1],p[2])
    dic = {}
    temp = [0,255]
    for i in temp:
        for j in temp:
            for k in temp:
                dic[(i,j,k)] = []
    barsize = img.size[0]//len(dic.keys())
    imgbar = Image.new("RGB",(img.size[0],img.size[1]+barsize),0)
    pix2 = imgbar.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pix2[x,y] = pix[x,y]
    keys = list(dic.keys())
    means = [(round(temp[0]),round(temp[1]),round(temp[2])) for temp in keys]
    for x in range(img.size[0]):
        for y in range(img.size[1],imgbar.size[1]):
            pix2[x,y] = means[int(x/(img.size[0]/K))]
    imgbar.show()
    return imgbar

#part 2
def kmeans(img):
    pix = img.load()
    store = dict()
    for x in range(img.size[0]):
            for y in range(img.size[1]):
                if pix[x,y] in store.keys():
                    store[pix[x,y]] = store[pix[x,y]] + 1
                else:
                    store[pix[x,y]] = 1
    dic0 = {}
    dic1 = {}

    centers = []
    while len(dic0)!=K:
        x = random.randint(0,img.size[0])
        y = random.randint(0,img.size[1])
        dic0[pix[x,y]] = []
        centers.append(pix[x,y])
        if pix[x,y] not in dic0.keys():
            temp = []
            for c in centers:
                temp.append(((pix[x,y][0]-c[0])**2 + (pix[x,y][1]-c[1])**2 + (pix[x,y][2]-c[2])**2)**0.5)
            if min(temp) > (img.size[0]*img.size[1]) / (K/2):
                dic0[pix[x,y]] = []
                centers.append(pix[x,y])

    
    count = 0
    while(True):
        print("Gen " + str(count) + ": " + str(dic0.keys()))
        count+=1
        print()
        
        for p in store.keys():
            dists = []
            for m in dic0.keys():
                err = (p[0]-m[0])**2 + (p[1]-m[1])**2 + (p[2]-m[2])**2
                dists.append((err,m))
            for i in range(store[p]):
                dic0[min(dists)[1]].append(p)
        for m in dic0.keys():
            temp = dic0[m]
            temp0 = [x[0] for x in temp]
            temp1 = [x[1] for x in temp]
            temp2 = [x[2] for x in temp]
            n0 = sum(temp0)/len(temp0)
            n1 = sum(temp1)/len(temp1)
            n2 = sum(temp2)/len(temp2)
            dic1[(n0,n1,n2)] = []
        if(dic1.keys() == dic0.keys()):
            return dic0
        dic0 = dic1
        dic1 = {}

def updateImg(img,dic):
    pix = img.load()
    for x in range(img.size[0]):
            for y in range(img.size[1]):
                dists = []
                for m in dic.keys():
                    err = (pix[x,y][0]-m[0])**2 + (pix[x,y][1]-m[1])**2 + (pix[x,y][2]-m[2])**2
                    dists.append((err,m))
                temp = min(dists)[1]
                pix[x,y] = (round(temp[0]),round(temp[1]),round(temp[2]))
    
    barsize = img.size[0]//len(dic.keys())
    imgbar = Image.new("RGB",(img.size[0],img.size[1]+barsize),0)
    pix2 = imgbar.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pix2[x,y] = pix[x,y]
    keys = list(dic.keys())
    means = [(round(temp[0]),round(temp[1]),round(temp[2])) for temp in keys]
    for x in range(img.size[0]):
        for y in range(img.size[1],imgbar.size[1]):
            pix2[x,y] = means[int(x/(img.size[0]/K))]
    imgbar.show()
    return imgbar,dic

def dithering(img,dic):
    pix = img.load()
    for y in range(img.size[1]):
            for x in range(img.size[0]):
                #old
                old = pix[x,y]
                #new
                dists = []
                for m in dic.keys():
                    err = (pix[x,y][0]-m[0])**2 + (pix[x,y][1]-m[1])**2 + (pix[x,y][2]-m[2])**2
                    dists.append((err,m))
                temp = min(dists)[1]
                #dither
                pix[x,y] = (round(temp[0]),round(temp[1]),round(temp[2]))
                ditherr = (old[0] - pix[x,y][0],old[1] - pix[x,y][1],old[2] - pix[x,y][2])
                if x+1<img.size[0] and y+1<img.size[1] and x-1>=0 and y-1>=0:
                    #print(ditherr)
                    pix[x+1,y] = (round(pix[x+1,y][0] + ditherr[0]* (7/16)),round(pix[x+1,y][1] + ditherr[1]* (7/16)),round(pix[x+1,y][2] + ditherr[2]* (7/16)))
                    pix[x,y+1] = (round(pix[x,y+1][0] + ditherr[0]* (5/16)),round(pix[x,y+1][1] + ditherr[1]* (5/16)),round(pix[x,y+1][2] + ditherr[2]* (5/16)))
                    pix[x-1,y+1] = (round(pix[x-1,y+1][0] + ditherr[0]* (3/16)),round(pix[x-1,y+1][1] + ditherr[1]* (3/16)),round(pix[x-1,y+1][2] + ditherr[2]* (3/16)))
                    pix[x+1,y+1] = (round(pix[x+1,y+1][0] + ditherr[0]* (1/16)),round(pix[x+1,y+1][1] + ditherr[1]* (1/16)),round(pix[x+1,y+1][2] + ditherr[2]* (1/16)))

    barsize = img.size[0]//len(dic.keys())
    imgbar = Image.new("RGB",(img.size[0],img.size[1]+barsize),0)
    pix2 = imgbar.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pix2[x,y] = pix[x,y]
    keys = list(dic.keys())
    means = [(round(temp[0]),round(temp[1]),round(temp[2])) for temp in keys]
    for x in range(img.size[0]):
        for y in range(img.size[1],imgbar.size[1]):
            pix2[x,y] = means[int(x/(img.size[0]/K))]
    imgbar.show()
    return imgbar


d = kmeans(img)
#u,t= updateImg(img,d)
u = dithering(img,d)
u.save("kmeansout.png")    

# check = set()
# pix = img.load()
# for y in range(img.size[1]):
#     for x in range(img.size[0]):
#         check.add(pix[x,y])

# print(check)
# print(len(check))


