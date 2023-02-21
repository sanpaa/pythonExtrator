import pandas as pd
from extrator import extrairdadosexcel
from observador import getquery
from consumidor import tratamentodata
from consumidor import tratamentotexto2

import os
import subprocess


df = pd.read_excel(f'C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\140_Copart 12.2022.xlsx', usecols="C,D,I,E,F,M,N,R,Z,O")


def NovoTratadorDeTexto(coluna):
    i = 0
    auxiliar = []
    for dados in coluna:
        dados = str(dados)
        dados = dados.replace(f'\n{i}', ",")
        if dados == "Nan" or dados == "nan" or dados == "NaN":
            dados = ""
        dados = dados.replace("[", "")
        dados = dados.replace("]", "")
        dados = dados.replace("'", "")
        auxiliar.append(dados)
        i = i + 1
    i = 0   # se existir mais linhas abaixo, se não, só retirar o while abaixo
    while i < 8:
        auxiliar.pop()
        i = i + 1
    return auxiliar


#df.iloc[:,[6]] - Titulo da col
#df.iloc[:,[6][0] - Conteudo da col


nome_prestador = df.iloc[:,[0][0]] # C
nome_prestador = NovoTratadorDeTexto(nome_prestador)
print(df)


numero_documento = df.iloc[:,[1][0]] # D
numero_documento = NovoTratadorDeTexto(numero_documento)

nome_usuario = df.iloc[:,[2][0]] # I
nome_usuario = NovoTratadorDeTexto(nome_usuario)

numero_doc_origem = df.iloc[:,[3][0]] # E
numero_doc_origem = NovoTratadorDeTexto(numero_doc_origem)

data_realização = df.iloc[:,[4][0]] # F
data_realização = NovoTratadorDeTexto(data_realização)
print(data_realização)

data_realização_tratada = tratamentodata(data_realização)
print(data_realização)

data_validade = df.iloc[:,[4][0]]
data_validade = NovoTratadorDeTexto(data_validade)
print(data_validade)

cod_procedimento = df.iloc[:,[5][0]]
cod_procedimento = NovoTratadorDeTexto(cod_procedimento)

descricao_procedimento = df.iloc[:,[6][0]]
descricao_procedimento = NovoTratadorDeTexto(descricao_procedimento)

contratante = df.iloc[:,[7][0]]
contratante = NovoTratadorDeTexto(contratante)

qtde_procedimento = df.iloc[:,[8][0]]
qtde_procedimento = NovoTratadorDeTexto(qtde_procedimento)

valor_coparticipacao = df.iloc[:,[9][0]]
valor_coparticipacao = NovoTratadorDeTexto(valor_coparticipacao)



# file1 = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste4.txt", 'w+')
# for i in descricao_procedimento:
#     file1.writelines(i + '\n')
#     file1.close
