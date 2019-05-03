# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:57:32 2019

@author: Student
"""

import getProducts
import random

HM = []
weight_value=10; #współczynnik wartości stosunku wagi maksymalnej do wagi rzeczywistej wózka
def genHM(CART_CAP, CART_MAX_WEIGHT, HM_CAP):
    HM = getProducts.getRandomProducts(CART_CAP, CART_MAX_WEIGHT ,HM_CAP)

    sort(HM,CART_CAP,HM_CAP) #sortowanie wózka po wadze
    CARTS_weight=[] #wagi poszczególnych wózków
    CARTS_price=[] #wartość poszczególnych wózków
    CARTS_value = [] #wartość wyznaczona przez wartość wózka i jego stosunku wagi do maksymalnej wagi wózka
    for i in range(len(HM)):
        weight = 0
        price = 0
        for j in range(len(HM[i])):
            if HM[i][j] is not None:
                weight = weight + HM[i][j].weight
                price = price + HM[i][j].price
            print(str(i+1)+"."+str(j+1)+" "+str(HM[i][j]))
        print('Waga: '+str(weight))
        CARTS_weight.append(weight)
        CARTS_price.append(price)
        weight=weight-CART_MAX_WEIGHT
        CARTS_value.append(price-(weight*weight_value))

    R1 = round(random.uniform(0,1),2)
    HMCR = .7
    HMS = CART_CAP * HM_CAP

    price=0
    weight=0
    cart_value=0
    x = []
    if R1 <= HMCR:
       print("---------------HMCR-------------------")
       for i in range(0,CART_CAP):
           l=random.randint(0, HM_CAP - 1)
           if(weight<=CART_MAX_WEIGHT and HM[l][i]!=None):
               weight = weight + HM[l][i].weight
               price=price+HM[l][i].price
               x.append(HM[random.randint(0, HM_CAP - 1)][i])
           else:
               x.append(None)

        #-----------------------------------PAR-----------------------------------
       #    R3 = round(random.uniform(0,1),2)
       #    PAR = .1
       #    #if R3 < PAR:     # BW z zakresu [-3;3]
       # R4 [-1;1]

    else:
        print("---------------R1-------------------")
        x=getProducts.getRandomProducts(CART_CAP,CART_MAX_WEIGHT,1);
        for i in range(0,CART_CAP):
            if x[i] is not None:
                weight=weight+x[i].weight
                price = price + x[i].price
    print("Prod:" + str(x))
    print("------------------------------------")
    print("weight: " + str(weight))
    print("price: " + str(price))
    cart_value=price-((weight-CART_MAX_WEIGHT)*10)
    print("Cart value: " + str(cart_value))
    #szukanie najgorszego wózka:
    numer=0;

    for i in range(0,HM_CAP):
        if i==0:
            worst=CARTS_value[i]
        else:
            if worst>CARTS_value[i]:
                worst=CARTS_value[i]
                numer=i
    print("Najgorszy wózek: "+str(numer+1)+" jego wartość: "+str(worst))

    #zamiana wózka w przypadku gdy nowy jest lepszy od najgorszego
    if cart_value>worst:
        print("Nowy wózek jest lepszy od najgorszego")
        HM[numer]=x
    else:
        print("Nowy wózek jest gorszy od najgorszego")



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
