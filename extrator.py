import pandas as pd
from observador import getquery
from consumidor import tratamentotextosimples
import os
import subprocess

def extrairdadosexcel(nomeentrada, nomesaida):
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


    if arquivo == 'Query vazia':
        raise SystemExit
        cmd = 'python consumidor.py'
        subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)

    df = pd.read_excel(f'C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\{arquivo[0]}', None) #usecols="A,B,C,F

    print(df['Planilha1']['Data Realizacao'])

    extrairdadosexcel('Nome Prestador','Nome_Prestador')
    extrairdadosexcel('Numero Documento','Numero_Documento')
    extrairdadosexcel('Nome Usuario','Nome_Usuario')
    extrairdadosexcel('Numero Doc Origem','Numero_Doc_Origem')
    extrairdadosexcel('Data Realizacao','Data_Realizacao')
    extrairdadosexcel('Data Realizacao','Data_Validade')
    extrairdadosexcel('Cod Procedimento','Cod_Procedimento')
    extrairdadosexcel('         Descricao Procedimento','Descricao_Procedimento')
    extrairdadosexcel('Contratante','Contratante')
    extrairdadosexcel('Qtde Procedimento','Qtde_Procedimento')
    extrairdadosexcel('Valor Coparticipacao','Valor_Coparticipacao')

    cmd = 'python consumidor.py'
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
