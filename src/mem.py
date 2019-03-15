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
    R1 = round(random.uniform(0,1),2)
    HMCR = .7
    HMS = CART_CAP * HM_CAP
    if R1 <= HMCR:
        x = []
        for i in range(0,CART_CAP):
            x.append(HM[i][random.randint(0, HM_CAP-1)])
        print("Prod:"+str(x))
        R3 = round(random.uniform(0,1),2)
        PAR = .1
        #if R3 < PAR:     # BW z zakresu [-3;3]
                         # R4 [-1;1]   

#def sort(HM):
    