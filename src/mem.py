# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:57:32 2019

@author: Student
"""

import getProducts
import random

HM = []

def genHM(CART_CAP, CART_MAX_WEIGHT, HM_CAP):
    HM = getProducts.getRandomProducts(CART_CAP, CART_MAX_WEIGHT ,HM_CAP)
    sort(HM,CART_CAP,HM_CAP) #sortowanie wózka po wadze
    for i in range(len(HM)):
        weight = 0
        for j in range(len(HM[i])):
            if HM[i][j] is not None:
                weight = weight + HM[i][j].weight
            print(str(i+1)+"."+str(j+1)+" "+str(HM[i][j]))
        print('Waga: '+str(weight))
    R1 = round(random.uniform(0,1),2)
    HMCR = .7
    HMS = CART_CAP * HM_CAP


    weight=0
    if R1 <= HMCR:
       print("---------------HMCR-------------------")
       x = []
       for i in range(0,CART_CAP):
           l=random.randint(0, HM_CAP - 1)
           if(weight<=CART_MAX_WEIGHT and HM[l][i]!=None):
               weight = weight + HM[l][i].weight
               x.append(HM[random.randint(0, HM_CAP - 1)][i])
           else:
               x.append(None)
       print("Prod:"+str(x))
       print("------------------------------------")
       print("weight: "+str(weight))
    else:
        print("---------------R1-------------------")
    #    R3 = round(random.uniform(0,1),2)
    #    PAR = .1
    #    #if R3 < PAR:     # BW z zakresu [-3;3]
                         # R4 [-1;1]   

def sort(HM,CART_CAP, HM_CAP):

    col = 0
    row = 0
    pcol=0
    temp = 0
    for x in range(0, HM_CAP):
        for y in range(0,CART_CAP):
            col = 0
            for z in range(0,CART_CAP):
                if not (col==0):
                    if not(HM[row][col]==None):
                        if HM[row][col].weight>HM[row][pcol].weight:
                            temp=HM[row][pcol]
                            HM[row][pcol]=HM[row][col]
                            HM[row][col]=temp
                pcol=col
                col+=1
        row+=1
