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
            for row in range(10000):
                res = cursor.execute(sql, ((myFactory.last_name() + str(random.randint(1,100))),float(random.uniform(1.0, 99.9)), float(random.uniform(1.0, 1000.0))))
                if res == 0:
                    print(str(row)+" : "+'Nie dodano rekordu')
            con.commit()
    except Exception as e:
        print(str(e))
    finally:
        con.close()