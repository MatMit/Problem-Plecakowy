# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql as mysql

con = mysql.connect(host='localhost',
                    user='root',
                    passwd='',
                    db='db',
                    charset='utf8mb4')
with con:
    cur = con.cursor()
    cur.execute('SELECT COUNT(id) FROM produkty')
    
    print(cur.fetchone()[0])
con.close()
