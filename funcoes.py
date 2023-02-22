import pandas as pd
import datetime

#df.iloc[:,[6]] - Titulo da col
#df.iloc[:,[6][0] - Conteudo da col
def TratadorDeTextoComplexo(coluna):
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

def tratamentotextosimples(document):
    variavel = document
    variavel = str(variavel)
    variavel = variavel.replace("[","") # )
    variavel = variavel.replace("]","") # )
    variavel = variavel.replace("'","") # )
    variavel = variavel.strip() # )
    variavel = variavel.split(',')
    return variavel
def tratamentotexto(document):
    variavel = document
    variavel = str(variavel)
    variavel = variavel.replace("[","") # )
    variavel = variavel.replace("]","") # )
    variavel = variavel.replace("'","") # )
    variavel = variavel.strip() # )
    print(variavel)
    # variavel = variavel[]
    variavel = variavel.split(',')
    print(variavel)

    return variavel

def tratamentodata(document):
    lista = []
    for elemento in document:
        data = str(elemento)
        data = datetime.datetime.strptime(elemento, '%Y-%m-%d %H:%M:%S')
        # data = data.strftime("%Y/%m/%d")
        data = data.strftime("%d/%m/%Y")
        data = str(data)
        lista.append(data)
    return lista


def CriarArquivo(nome,conteudo):
    variavel = nome
    nome = open(f"C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\{nome}.txt", 'w+')
    for elemento in conteudo:
        nome.writelines(elemento + ',')
    nome.close()
# file1 = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste4.txt", 'w+')
# for i in descricao_procedimento:
#     file1.writelines(i + '\n')
#     file1.close
