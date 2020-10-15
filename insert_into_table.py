#!/home/etokral/Python_projs/postgreSQL/bin/python
import psycopg2
from config import config

def insert_into_table(starList):
    sql = """ INSERT INTO starstb1 (
        cnsName, raH, raM, raS, decD, decAM, decAS, trigPAR, specTYPE, vMAG, comNAME)
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        cur.executemany(sql, starList)

        conn.commit()

        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    #starList = ('GJ  551', 14, 29, 43.0, -62, 40, 46, 0.76885, 'M5.0', 11.05, 'Proxima Centauri')
    #starList = [('GJ  551', 14, 29, 43.0, -62, 40, 46, 0.76885, 'M5.0', 11.05, 'Proxima Centauri'),
    #('GJ  559', 14, 39, 36.5, -60, 50, 2, 0.74723, 'G2.0', 0.01, 'alpha Centauri A')]
    #insert_into_table(starList)
    with open('db100Data.txt', 'r') as fajl:
        for line in fajl:
            print(line)
