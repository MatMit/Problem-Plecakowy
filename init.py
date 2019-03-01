# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql as mysql

def init():
    con = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        db='db',
                        charset='utf8mb4')
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT COUNT(id) FROM produkty')
            
            rows = cur.fetchone()[0]
            if rows == 0:
                print("Brak wpisow")
            else:
                print("Liczba wpisow: "+str(rows))
        con.close()
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    init()
    