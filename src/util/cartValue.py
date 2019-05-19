def cartValue(cart):
    value = 0
    for i in range (0,len(cart)):
        cartObj = cart[i]
        value += cartObj.price
    return value
