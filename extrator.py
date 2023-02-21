import pandas as pd
from observador import getquery
from consumidor import tratamentotextosimples
import os
import subprocess


def extrairdadosexcel(nomeentrada, nomesaida,df):
    file1 = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\" + nomesaida + ".txt", 'w+')
    for i in df["Planilha1"][nomeentrada]:
        b = i
        b = str(b)
        print(b)
        if b == 'NaN' or b == 'nan' or b == 'Nan' or b == 'NaT':
            continue
        else:
            file1.write(',')
        file1.writelines(b)
    file1.close()

if __name__ == '__main__':
    arquivo = getquery()
    arquivo = tratamentotextosimples(arquivo)
    print(arquivo[0])
    continuar = 0
    if arquivo[0] != 'Query vazia':
        print("continuar 1")
        continuar = 1
    if arquivo[0] == 'Query vazia' or continuar == 0:
        print("continuar 0")
        print("Voltando pro observador...")
        exec(open("./observador.py").read())
        exit()


    if continuar == 1 and arquivo[0] != 'Query vazia':
        df = pd.read_excel(f'C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\{arquivo[0]}', None) #usecols="A,B,C,F

        extrairdadosexcel('Nome Prestador','Nome_Prestador',df)
        extrairdadosexcel('Numero Documento','Numero_Documento',df)
        extrairdadosexcel('Nome Usuario','Nome_Usuario',df)
        extrairdadosexcel('Numero Doc Origem','Numero_Doc_Origem',df)
        extrairdadosexcel('Data Realizacao','Data_Realizacao',df)
        extrairdadosexcel('Data Realizacao','Data_Validade',df)
        extrairdadosexcel('Cod Procedimento','Cod_Procedimento',df)
        extrairdadosexcel('         Descricao Procedimento','Descricao_Procedimento',df)
        extrairdadosexcel('Contratante','Contratante',df)
        extrairdadosexcel('Qtde Procedimento','Qtde_Procedimento',df)
        extrairdadosexcel('Valor Coparticipacao','Valor_Coparticipacao',df)

        print("Indo pro consumidor...")
        exec(open("./consumidor.py").read())
        exit()


