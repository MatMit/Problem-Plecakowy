# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:44:54 2019

@author: Student
"""

import pymysql as mysql
import random
from product import Product

def getRandomProducts(CART_CAP, CART_MAX_WEIGHT ,HM_CAP):
    HM = []
    con = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        db='db',
                        charset='utf8mb4')
    try:
        sql = "SELECT id, weight, price FROM products WHERE id = %s"
        with con.cursor() as cur:
            if HM_CAP==1:
                weigth = 0
                print("test")
                for j in range(CART_CAP):
                    if weigth<= CART_MAX_WEIGHT:
                        cur.execute(sql, (random.randint(1,10000)))
                        row = cur.fetchone()
                        HM.append(Product(row[0], row[1], row[2]))
                        weigth = weigth + row[1]
                    else:
                        HM.append(None)

            else:
                for i in range(HM_CAP):
                    temp = []
                    weigth = 0
                    for j in range(CART_CAP):
                        if weigth<= CART_MAX_WEIGHT:
                            cur.execute(sql, (random.randint(1,10000)))
                            row = cur.fetchone()
                            temp.append(Product(row[0], row[1], row[2]))
                            weigth = weigth + row[1]
                        else:
                            temp.append(None)

                    HM.append(temp)

        return HM
    except Exception as e:
        print("GetProducts:"+str(e))
    