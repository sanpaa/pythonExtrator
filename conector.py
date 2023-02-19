import cx_Oracle
import os
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
userdb = os.getenv("cst_dbora")
passwdb = os.getenv("als_dbora")
enderdb = os.getenv("ender_dbora")
namedb = os.getenv("nm_dbora")

cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\paulo.sanches\Desktop\instantclient_21_9")

connection = cx_Oracle.connect(f"{userdb}/{passwdb}@{enderdb}/{namedb}")

cursor = connection.cursor()

def executeSQL(sql,dados):
    connection = cx_Oracle.connect(f"{userdb}/{passwdb}@{enderdb}/{namedb}")
    cursor = connection.cursor()
    cursor.execute(sql,dados)
    connection.commit()
    cursor.close()

connection.commit()

cursor.close()
