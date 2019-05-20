import init as const
from product import Product

import pymysql as mysql
import random

def getRandomProducts(amount):
    HM = []
    con = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        db='db',
                        charset='utf8mb4')
    try:
        sql = "SELECT id, weight, price FROM products WHERE id = %s"
        with con.cursor() as cur:
            if amount==1:
                weigth = 0
                for j in range(const.CART_CAP):
                    if weigth<= const.CART_MAX_WEIGHT:
                        cur.execute(sql, (random.randint(1,10000)))
                        row = cur.fetchone()
                        HM.append(Product(row[0], row[1], row[2]))
                        weigth = weigth + row[1]
                    else:
                        HM.append(None)

            else:
                for i in range(amount):
                    temp = []
                    weigth = 0
                    for j in range(const.CART_CAP):
                        if weigth<= const.CART_MAX_WEIGHT:
                            cur.execute(sql, (random.randint(1,10000)))
                            row = cur.fetchone()
                            temp.append(Product(row[0], row[1], row[2]))
                            weigth = weigth + row[1]
                        else:
                            temp.append(None)

                    HM.append(temp)
            con.close()

        return HM
    except Exception as e:
        print("GetProducts:"+str(e))
