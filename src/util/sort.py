import init as const

## Sortowanie wózka po wagach
def sort(HM):
    col = 0
    row = 0
    pcol=0
    temp = 0
    for x in range(0, const.HM_CAP):
        for y in range(0,const.CART_CAP):
            col = 0
            for z in range(0,const.CART_CAP):
                if not (col==0):
                    if not(HM[row][col]==None):
                        if HM[row][col].weight>HM[row][pcol].weight:
                            temp=HM[row][pcol]
                            HM[row][pcol]=HM[row][col]
                            HM[row][col]=temp
                pcol=col
                col+=1
        row+=1
