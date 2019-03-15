# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 12:44:54 2019

@author: Student
"""

import pymysql as mysql
import random
from product import Product

def getRandomProducts(CART_CAP, HM_CAP):
    HM = []
    con = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        db='db',
                        charset='utf8mb4')
    try:
        sql = "SELECT id, weight, price FROM products WHERE id = %s"
        with con.cursor() as cur:
            for i in range(HM_CAP):
                temp = []
                for j in range(CART_CAP):
                    cur.execute(sql, (random.randint(1,10000),))
                    row = cur.fetchone()
                    temp.append(Product(row[0], row[1], row[2]))
                HM.append(temp)
        return HM
    except Exception as e:
        print("GetProducts:"+str(e))
    