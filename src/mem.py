import getProducts as getProducts
import init as const
import util.sort as sort
import util.findLowCart as findLowCart
import util.cartValue as cartValueFunc

import random
import numpy as np
import matplotlib.pyplot as plt

WEIGHT_VALUE=10; #współczynnik wartości stosunku wagi maksymalnej do wagi rzeczywistej wózka
HMCR = .7
PAR = .5
HMS = const.CART_CAP * const.HM_CAP

def genHM():
    HM = getProducts.getRandomProducts(const.HM_CAP)
        
    iter = 1
    xplot = []
    yplot = []
    while iter<=20000:
        xplot.append(iter)
        sort.sort(HM) #sortowanie wózka po wadze
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
            CARTS_weight.append(weight)
            CARTS_price.append(price)
            weight=weight-const.CART_MAX_WEIGHT
            CARTS_value.append(price-(weight*WEIGHT_VALUE))
        R1 = round(random.uniform(0,1),2)
        R3 = round(random.uniform(0,1),2)
        
        price=0
        weight=0
        cartValue=0
        x = []
        if R1 <= HMCR:                                                              # Improwizacja HMCR?
           #print("---------------HMCR-------------------")
           for i in range(0,const.CART_CAP):    #
               l=random.randint(0, const.HM_CAP-1)
               if(weight<=const.CART_MAX_WEIGHT and HM[l][i]!=None):
                   weight = weight + HM[l][i].weight
                   price=price+HM[l][i].price
                   x.append(HM[l][i])
               else:
                   x.append(None)
           if R3 <= PAR:                                                            # Improwizacja PAR?
               #print("---------------PAR-------------------")
               price = 0
               weight = 0
               oldPrice = 0
               oldWeight = 0
               oldCart_value = 0
               lowWeightProduct = HM[0][0]
               randomProductIndex = random.randint(0, const.CART_CAP - 1)
               randomProduct = x[randomProductIndex]
               while randomProduct == None: #jesli wylosowałem produkt None, to szukam innego losowego produktu
                   randomProductIndex = random.randint(0, const.CART_CAP - 1)
                   randomProduct = x[randomProductIndex]
                   
    
               for y in range(len(HM)): #szukanie produktu o najniższej wadze w pamięci HM
                   for z in range(len(HM[y])):
                       if(HM[y][z]!=None):
                           if(lowWeightProduct.weight > HM[y][z].weight):
                               lowWeightProduct = HM[y][z]

               for y in range(len(HM)): #szukanie produktu o trochę niższej wadze niż wylosowany produkt z koszyka
                   for z in range(len(HM[y])):
                       if(HM[y][z]!=None):
                           if(HM[y][z].weight < randomProduct.weight and  HM[y][z].weight > lowWeightProduct.weight):
                               lowWeightProduct = HM[y][z]
                               
               oldProduct = x[randomProductIndex]

               for i in range(0,const.CART_CAP):
                   if x[i] is not None:
                       oldWeight = oldWeight + x[i].weight
                       oldPrice = oldPrice + x[i].price

               oldCart_value=calcCartValue(oldPrice,oldWeight)
               x[randomProductIndex] = lowWeightProduct
               price = 0
               weight = 0

               for i in range(0,const.CART_CAP):
                   if x[i] is not None:
                       weight = weight + x[i].weight
                       price = price + x[i].price
               cart_value=calcCartValue(price,weight)

               if cart_value < oldCart_value:
                   x[randomProductIndex] = oldProduct
                   price = oldPrice
                   weight = oldWeight
                   cart_value = oldCart_value


                   

          
        else:                                                                       # Improwizacja losowa?
            #print("---------------Improwizacja losowa-------------------")
            x=getProducts.getRandomProducts(1)
            for i in range(0,const.CART_CAP):
                if x[i] is not None:
                    weight=weight+x[i].weight
                    price = price + x[i].price
        cartValue = calcCartValue(price,weight)
        
        #szukanie najgorszego wózka:
        cartNum=0;
    
        for i in range(0,const.HM_CAP):
            if i==0:
                worstValue=CARTS_value[i]
            else:
                if worstValue>CARTS_value[i]:
                    worstValue=CARTS_value[i]
                    cartNum=i
        
        #zamiana wózka w przypadku gdy nowy jest lepszy od najgorszego
        if cartValue>worstValue:
            print(str(iter) + ": Nowy wózek"+ str(cartValueFunc.cartValue(x))  +" jest lepszy od najgorszego "+ str(cartValueFunc.cartValue(HM[cartNum]))+" \r\nworst/new "+str(worstValue)+"/"+str(cartValue))
            HM[cartNum]=x
        #else:
            #print(str(iter) + ": Nowy wózek jest gorszy od najgorszego")
        yplot.append(cartValueFunc.cartValue(HM[findLowCart.findLowestCartValue(HM)]))
        iter=iter+1
    print("x: "+str(len(xplot))+"\r\ny:"+str(len(yplot)))
    drawGraph(xplot,yplot)
    

def calcCartValue(price, weight):
    return price - (weight-const.CART_MAX_WEIGHT)*WEIGHT_VALUE
    

def drawGraph(x,y):
    plt.xlabel('Iteracja')
    plt.ylabel('Wartosc')
    plt.title('Wartosc najgorszego wozka po iteracjach')
    plt.plot(x,y,'bo')
