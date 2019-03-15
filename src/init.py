# -*- coding: utf-8 -*-

import pymysql as mysql
import database.db as db
#from product import product
import mem

def init():
    CART_CAP = 5   # pojemnosc wozka
    HM_CAP = 5     # ilosc wozkow
    
    
    con = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        db='db',
                        charset='utf8mb4')
    try:
        with con.cursor() as cursor:
            cursor.execute('CREATE TABLE IF NOT EXISTS products (id int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(90) NOT NULL, weight decimal(5,2) NOT NULL, price decimal(7,2) NOT NULL)')
        con.commit()
        
        with con:
            cur = con.cursor()
            cur.execute('SELECT COUNT(id) FROM products')
            
            rows = cur.fetchone()[0]
            if rows == 0:
                db.prepareDatabase()
        con.close()
        mem.genHM(CART_CAP, HM_CAP)
    except Exception as e:
        print("Init:"+str(e))

if __name__ == "__main__":
    init()
