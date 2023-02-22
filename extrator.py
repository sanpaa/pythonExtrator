import pandas as pd
from observador import getquery
from funcoes import *
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
        df = pd.read_excel(f'C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\{arquivo[0]}', usecols="C,D,E,F,I,M,N,O,R,Z") #usecols="A,B,C,F

        nome_prestador = df.iloc[:, [0][0]]  # C
        nome_prestador = TratadorDeTextoComplexo(nome_prestador)
        variavel = 'Nome_Prestador'
        CriarArquivo(variavel,nome_prestador)

        numero_documento = df.iloc[:, [1][0]]  # D
        numero_documento = TratadorDeTextoComplexo(numero_documento)
        variavel = 'Numero_Documento'
        CriarArquivo(variavel,numero_documento)

        numero_doc_origem = df.iloc[:, [2][0]]  # E
        numero_doc_origem = TratadorDeTextoComplexo(numero_doc_origem)
        variavel = 'Numero_Doc_Origem'
        CriarArquivo(variavel,numero_doc_origem)


        data_realização = df.iloc[:, [3][0]]  # F
        data_realização = TratadorDeTextoComplexo(data_realização)
        data_realização = tratamentodata(data_realização)
        variavel = 'Data_Realizacao'
        CriarArquivo(variavel,data_realização)

        data_validade = df.iloc[:, [3][0]]
        data_validade = TratadorDeTextoComplexo(data_validade)
        data_validade = tratamentodata(data_validade)
        variavel = 'Data_Validade'
        CriarArquivo(variavel,data_validade)

        nome_usuario = df.iloc[:, [4][0]]  # I
        nome_usuario = TratadorDeTextoComplexo(nome_usuario)
        variavel = 'Nome_Usuario'
        CriarArquivo(variavel,nome_usuario)

        cod_procedimento = df.iloc[:, [5][0]]
        cod_procedimento = TratadorDeTextoComplexo(cod_procedimento)
        variavel = 'Cod_Procedimento'
        CriarArquivo(variavel,cod_procedimento)


        descricao_procedimento = df.iloc[:, [6][0]]
        descricao_procedimento = TratadorDeTextoComplexo(descricao_procedimento)
        variavel = 'Descricao_Procedimento'
        CriarArquivo(variavel,descricao_procedimento)


        contratante = df.iloc[:, [8][0]]
        contratante = TratadorDeTextoComplexo(contratante)
        variavel = 'Contratante'
        CriarArquivo(variavel,contratante)

        qtde_procedimento = df.iloc[:, [9][0]]
        qtde_procedimento = TratadorDeTextoComplexo(qtde_procedimento)
        variavel = 'Qtde_Procedimento'
        CriarArquivo(variavel,qtde_procedimento)

        valor_coparticipacao = df.iloc[:, [7][0]]
        valor_coparticipacao = TratadorDeTextoComplexo(valor_coparticipacao)
        variavel = 'Valor_Coparticipacao'
        CriarArquivo(variavel,valor_coparticipacao)


        print("Indo pro consumidor...")
        exec(open("./consumidor.py").read())
        exit()


