import mem
def cartValue(cart):
    value = 0
    weight = 0
    for i in range (0,len(cart)):
        cartObj = cart[i]
        if cartObj != None:
            value += cartObj.price
            weight += cartObj.weight
    #print(str(value)+" "+str(weight)+" ="+str(mem.calcCartValue(value,weight)))
    return mem.calcCartValue(value,weight)

def isCartInHM(cart, HM):
    for i in range(len(HM)):
        if cartValue(cart) == cartValue(HM[i]):
            return True
    return False
