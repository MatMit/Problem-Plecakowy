from util.cartValue import cartValue

def findLowestCartValue(HM):
    value = cartValue(HM[0])
    id = 0
    for i in range(1,len(HM)):
        if value > cartValue(HM[i]):
            id = i
    return id
