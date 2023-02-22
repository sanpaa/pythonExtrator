import conector
from datetime import datetime
from observador import *
from funcoes import *
import time
import os
import shutil


if __name__ == '__main__':
    datahora = getDataHoraInicial()
    data = getDataInicial()
    try:
        arquivo_log = open(f"C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Log_banco_{datahora}.txt", 'w')
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
    except FileNotFoundError:
        print("Faltam arquivos, então, voltando pro extrator.")
        exec(open("./extrator.py").read())
        exit()

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
    Data_Realizacao_Tratado = List_Data_Realizacao
    Data_Validade_Tratado = List_Data_Validade

    i = 0
    print(len(List_Numero_Documento))
    lista_log = []
    while i < (len(List_Numero_Documento ) - 1):
        sql = """
            insert into custom_tasy.AUX_copart_lojas_cem_fesp         
            (SEQ,NNUMEUSUA,NTITUUSUA,COMPETENCIA,RESPONSAVEL,NUMERO,NOME,DOC,DATA_ATENDIMENTO,DATA_VENCIMENTO,CODIGO_SERVICO,DESCRICAO,NOME_PRESTADOR,QUANTIDADE,VALOR_COPARTICIPACAO)
            values 
            (custom_tasy.copart_lojas_cem_fesp_seq.nextval,:num,:numusu,:comp,:respon,:numero,:nome_grande,:doc,to_date(:dt_atendimento,'dd/mm/yyyy'),to_date(:dt_atendimento_final,'dd/mm/yyyy'),:codigo_serv,:descricao,:nome_prest,:qty,:valor_copart)
        """
        linha = [231,21,22,List_Nome_prestador[i],40,List_Nome_Usuario[i],List_Numero_Documento[i],Data_Realizacao_Tratado[i],Data_Validade_Tratado[i],83537,List_Descricao_Procedimento[i],List_Nome_prestador[i],List_Qtde_Procedimento[i],List_Valor_Coparticipacao[i]]
        # conector.executeSQL(sql,linha) # data direto no execute sql retorna erro.
        lista_log.append(linha)
        i = i + 1


    i = 0
    for elemento in lista_log:
        arquivo_log.writelines(str(i) + ': '+str(elemento)+'\n')
        time.sleep(0.0001)
        i = i + 1
    arquivo_log.writelines(f"\nForam inseridas {i} linhas.\n")
    arquivo_log.writelines("Na data e hora: " + datahora)
    arquivo_log.close()
    query = getquery()
    moverArquivos = moverArquivos(data,datahora,query[0])
    if moverArquivos == 'Faltam arquivos.':
        print("Faltam arquivos, então, voltando pro extrator.")
        exec(open("./extrator.py").read())
        exit()
    #Final
    print("acabou, voltando a observar")

    exec(open("./observador.py").read())
    exit()

