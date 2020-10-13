#!/home/etokral/Python_projs/postgreSQL/bin/python
import psycopg2
from config import config

def create_tables():
    command = (
        """
        CREATE TABLE starstb1 (
        id smallserial PRIMARY KEY,
        cnsName varchar(20) NOT NULL,
        raH smallint,
        raM smallint,
        raS real,
        raRAD real,
        decD smallint,
        decAM smallint,
        decAS smallint,
        decRAD real,
        trigPAR real,
        distLY real,
        specTYPE varchar(10),
        vMAG real,
        comNAME varchar(50)
        );
        """)

    conn = None
    try:
        params = config()

        conn = psycopg2.connect(**params)

        cur = conn.cursor()

        print(command)
        cur.execute(command)

        cur.close()

        conn.commit()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()
