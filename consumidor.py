import conector
import datetime
import os
import subprocess
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
    variavel = variavel[1:]
    variavel = variavel.split(',')
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

if __name__ == '__main__':
    Nome_prestador = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Nome_Prestador.txt", 'r')
    Nome_prestador = Nome_prestador.readlines()
    Numero_Documento = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Numero_Documento.txt", 'r')
    Numero_Documento = Numero_Documento.readlines()
    Nome_Usuario = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Nome_Usuario.txt", 'r')
    Nome_Usuario = Nome_Usuario.readlines()
    Numero_Doc_Origem = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Numero_Doc_Origem.txt", 'r')
    Numero_Doc_Origem = Numero_Doc_Origem.readlines()
    Data_Realizacao = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Data_Realizacao.txt", 'r')
    Data_Realizacao = Data_Realizacao.readlines()
    Data_Validade = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Data_Validade.txt", 'r')
    Data_Validade = Data_Validade.readlines()
    Descricao_Procedimento = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Descricao_Procedimento.txt", 'r')
    Descricao_Procedimento = Descricao_Procedimento.readlines()
    Contratante = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Contratante.txt", 'r')
    Contratante = Contratante.readlines()
    Qtde_Procedimento = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Qtde_Procedimento.txt", 'r')
    Qtde_Procedimento = Qtde_Procedimento.readlines()
    Valor_Coparticipacao = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Valor_Coparticipacao.txt", 'r')
    Valor_Coparticipacao = Valor_Coparticipacao.readlines()

    #Tratamento de Texto/Data
    List_Nome_prestador = tratamentotexto(Nome_prestador)
    List_Numero_Documento = tratamentotexto(Numero_Documento)
    List_Nome_Usuario = tratamentotexto(Nome_Usuario)
    List_Numero_Doc_Origem = tratamentotexto(Numero_Doc_Origem)
    List_Data_Realizacao = tratamentotexto(Data_Realizacao)
    List_Data_Validade = tratamentotexto(Data_Validade)
    List_Descricao_Procedimento = tratamentotexto(Descricao_Procedimento)
    List_Contratante = tratamentotexto(Contratante)
    List_Qtde_Procedimento = tratamentotexto(Qtde_Procedimento)
    List_Valor_Coparticipacao = tratamentotexto(Valor_Coparticipacao)

    #Tratamento Especifico para Data
    Data_Realizacao_Tratado = tratamentodata(List_Data_Realizacao)
    Data_Validade_Tratado = tratamentodata(List_Data_Validade)

    i = 0
    while i < len(List_Numero_Documento):
        sql = """
            insert into custom_tasy.AUX_copart_lojas_cem_fesp
            (SEQ,NNUMEUSUA,NTITUUSUA,COMPETENCIA,RESPONSAVEL,NUMERO,NOME,DOC,DATA_ATENDIMENTO,DATA_VENCIMENTO,CODIGO_SERVICO,DESCRICAO,NOME_PRESTADOR,QUANTIDADE,VALOR_COPARTICIPACAO)
            values (:seq,:num,:numusu,:comp,:respon,:numero,:nome_grande,:doc,to_date(:dt_atendimento,'dd/mm/yyyy'),to_date(:dt_atendimento_final,'dd/mm/yyyy'),:codigo_serv,:descricao,:nome_prest,:qty,:valor_copart)
            """
        linha = [i+1985,231,21,22,List_Nome_prestador[i],40,List_Nome_Usuario[i],List_Numero_Documento[i],Data_Realizacao_Tratado[i],Data_Validade_Tratado[i],83537,List_Descricao_Procedimento[i],List_Nome_prestador[i],List_Qtde_Procedimento[i],List_Valor_Coparticipacao[i]]
        conector.executeSQL(sql,linha) # data direto no execute sql retorna erro.
        i = i + 1
else:
    cmd = 'python observador.py'
    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)

