# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:57:32 2019

@author: Student
"""

import getProducts
import random

HM = []



def genHM(CART_CAP, HM_CAP):
    HM = getProducts.getRandomProducts(CART_CAP, HM_CAP)
    sort(HM,CART_CAP, HM_CAP);
    for y in HM:
        for z in y:
            print(z.weight)

    R1 = round(random.uniform(0,1),2)
    HMCR = .7
    HMS = CART_CAP * HM_CAP
    if R1 <= HMCR:
        x = []
        for i in range(0,CART_CAP):
            x.append(HM[i][random.randint(0, HM_CAP-1)])
        #print("Prod:"+str(x))
        R3 = round(random.uniform(0,1),2)
        PAR = .1
        #if R3 < PAR:     # BW z zakresu [-3;3]
                         # R4 [-1;1]   

def sort(HM,CART_CAP, HM_CAP):

    col = 0
    row = 0
    temp = 0
    for i in range(0,CART_CAP*HM_CAP):
        row=0
        for y in range(0,HM_CAP):
            col = 0
            for z in range(0,CART_CAP):
                if not (col==0 and row==0):
                    #print("previous")
                    #print("row: "+str(prow)+" col: "+str(pcol)+" weight: "+str(HM[prow][pcol].weight))
                    #print("Now")
                    #print("row: " + str(row) + " col: " + str(col) + " weight: " + str(HM[row][col].weight))
                    if HM[row][col].weight>HM[prow][pcol].weight:
                        temp=HM[prow][pcol]
                        HM[prow][pcol]=HM[row][col]
                        HM[row][col]=temp
                prow=row
                pcol=col
                col+=1
            row+=1
