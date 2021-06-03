path = '/Users/SJC/Documents/chinook/db/test_data.db'
data = [("James", "Butt", "jbutt@gmail.com"), ("Art", "Venere", "art@venere.org"), ("Lenna", "Paprocki", "lpaprocki@hotmail.com"), ("Donette", "Foller", "donette.foller@cox.net"), ("Simona", "Morasca", "simona@morasca.com"), ("Mitsue", "Tollner", "mitsue_tollner@yahoo.com"), ("Leota", "Dilliard", "leota@hotmail.com"), ("Sage", "Wieser", "sage_wieser@cox.net"), ("Kris", "Marrier", "kris@gmail.com")]

import sqlite3
from sqlite3 import Error
import csv

def create_connection(path):
    con = None
    try:
        con = sqlite3.connect(path)
        print(f'Connection to SQLite {path} DB sucessfull')
    except Error as er:
        print(f'An error {er} has occured')
    return con


def create_tables():
    con = create_connection(path)
    cur = con.cursor()

    student_register ='''CREATE TABLE IF NOT EXISTS STUDENT_REGISTER(
   STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
   FIRST_NAME VARCHAR(20) NOT NULL,
   LAST_NAME VARCHAR(20),
   DATE_ENROLLOED VARCHAR,
   EMAIL VARCHAR(320))'''

    courses ='''CREATE TABLE IF NOT EXISTS COURSES(
   COURSE_ID INTEGER PRIMARY KEY,
   COURSE_NAME VARCHAR(20) NOT NULL,
   COURSE_PRICE VARCHAR(20),
   FOREIGN KEY (COURSE_NAME) REFERENCES "STUDENT_ID" (COURSE_NAME))'''
   

    for tables in [student_register, courses]:
       
        try:
            cur.execute(tables)
            print(f'{tables} created')
        except Error as er:
            print(f'{tables} not created, an error {er}')
            pass
        
def import_data():
    con = create_connection(path)
    cur = con.cursor()

    
    try:
        sql_insert = """INSERT INTO STUDENT_REGISTER (FIRST_NAME, LAST_NAME, EMAIL)
                      VALUES
                      (?, ?, ?)"""
        cur.executemany(sql_insert, data)
        con.commit()
        print('Total ', cur.rowcount, 'Records inserted correctly')
        index = """"CREATE UNIQUE INDEX index_email
                    ON STUDENT_REGISTER (EMAIL)"""
        cur.execute(index)

        cur.close

    except sqlite3.Error as error:
        print('Failed to instert multiple recordss  into sqlite table')

    finally:
        if con:
            con.close()
            print('The sqlite connection is closed')    
                            
def main(path):
    
    create_tables()
    import_data()

if __name__ == '__main__':
    main(path)
        
