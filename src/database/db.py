import pymysql as mysql
from faker import Faker
import random

def prepareDatabase():
    con = mysql.connect(host='localhost',
                        user='root',
                        passwd='',
                        db='db',
                        charset='utf8mb4')

    try:
        with con.cursor() as cursor:
            myFactory = Faker()
            sql = 'INSERT INTO products(name, weight, price) VALUES(%s, %s, %s)' #%f wyrzuca 'must be real number, not str'...
            for row in range(10001):
                res = cursor.execute(sql, ((myFactory.last_name() + str(random.random()*100+1)),float(random.uniform(1.0, 12.5)), float(random.uniform(1.0, 1000.0))))
                if res == 1:
                    print(str(row)+" : "+'Dodano wpis')
            con.commit()
    finally:
        con.close()