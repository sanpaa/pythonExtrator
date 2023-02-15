import cx_Oracle
import datetime as dt
cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\paulo.sanches\Desktop\instantclient_21_9")

#dsn = cx_Oracle.makedsn(host='tasyora-scan.unimedsaltoitu.local', port=1521)
connection = cx_Oracle.connect("paulos/unimed@tasyora-scan.unimedsaltoitu.local:1521/TASY")
# metodo de conexão 2 abaixo
# connection = cx_Oracle.connect(user="paulos", password='unimed',
#                              dsn=dsn,
#                              encoding="UTF-8")

cursor = connection.cursor()

# prepare data insertion rows
dataInsertionTuples = [

]

b = "joao", dt.datetime(2021, 1, 1), 155
# create sql for data insertion

# execute the sql to perform data extraction
cursor.execute(sqlTxt)
while True:
    row = cursor.fetchone()
    if row is None:
        break
    print(row)
    print("\n")

rowCount = cursor.rowcount
print("number of inserted rows =", rowCount)

connection.commit()

cursor.close()