import cx_Oracle
import datetime as dt

cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\paulo.sanches\Desktop\instantclient_21_9")

# dsn = cx_Oracle.makedsn(host='tasyora-scan.unimedsaltoitu.local', port=1521)
connection = cx_Oracle.connect("custom_tasy/aloisk@192.168.0.223:1521/tasyt")

cursor = connection.cursor()

sqlTxt = """select * from custom_tasy.AUX_copart_lojas_cem_fesp"""

# execute the sql to perform data extraction
cursor.execute(sqlTxt)
file1 = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste2.txt", mode='w')

row = cursor.fetchone()
b = row
b = str(b)


def executeSQL(sql,dados):
    connection = cx_Oracle.connect("custom_tasy/aloisk@192.168.0.223:1521/tasyt")
    cursor = connection.cursor()
    cursor.execute(sql,dados)
    connection.commit()
    cursor.close()

# while True:
#     #b = b.replace(",","") # ,
#     #b = b.replace(")","") # )
#     #b = b.replace("(","") # (
#     #b = b.replace("'","") # '
#     #b = b.replace("datetime","") # datetime
#     #b = b.replace(".2023", "")  # datetime
#     file1.writelines(b)
#     file1.write('\n')
#
#
#     if row is None:
#         break


#file1.close()

#manipulação do arquivo / tratando arquivo não existente
#try:
 #   f = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste2.txt", "r")
 #   a = f.readlines()
    #for linha in a:
        #print(linha, "\n")
#    #print(len(a))
#   f.close()
#except FileNotFoundError:
#    f = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste2.txt", 'w+')
#    a = f.writelines("Vazio")
#    f.close()
#    print("Arquivo não encontrado, porém, criado.")

#conta as linhas do select
rowCount = cursor.rowcount
print("number of inserted rows =", rowCount)

connection.commit()

cursor.close()
