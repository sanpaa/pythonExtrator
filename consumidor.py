import conector

Nome_prestador = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Nome_Prestador.txt", 'r')
Numero_Documento = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Numero_Documento.txt", 'r')
Nome_Usuario = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Nome_Usuario.txt", 'r')
Numero_Doc_Origem = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Numero_Doc_Origem.txt", 'r')
Data_Realizacao = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Data_Realizacao.txt", 'r')
Data_Validade = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Data_Validade.txt", 'r')
Descricao_Procedimento = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Descricao_Procedimento.txt", 'r')
Contratante = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Contratante.txt", 'r')
Qtde_Procedimento = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Qtde_Procedimento.txt", 'r')
Valor_Coparticipacao = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Valor_Coparticipacao.txt", 'r')


def tratamentotexto(document):
    variavel = document.readlines()
    variavel = str(variavel)
    variavel = variavel.replace("[","") # )
    variavel = variavel.replace("]","") # )
    variavel = variavel.replace("'","") # )
    variavel = variavel.strip() # )
    variavel = variavel[1:]
    variavel = variavel.split(',')
    return variavel

List_Nome_prestador = tratamentotexto(Nome_prestador)
List_Numero_Documento = tratamentotexto(Numero_Documento)
List_Nome_Usuario = tratamentotexto(Nome_Usuario)
List_Numero_Doc_Origem = tratamentotexto(Numero_Doc_Origem)
List_Data_Realizacao = tratamentotexto(Data_Realizacao)
List_Data_Validade = tratamentotexto(Data_Validade)
Descricao_Procedimento = tratamentotexto(Descricao_Procedimento)
Contratante = tratamentotexto(Contratante)
Qtde_Procedimento = tratamentotexto(Qtde_Procedimento)
Valor_Coparticipacao = tratamentotexto(Valor_Coparticipacao)

i = 0
resultado = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\Resultado.txt", 'w+')

while i < len(List_Numero_Documento):
    sql = """insert into custom_tasy.AUX_copart_lojas_cem_fesp
        (SEQ,NNUMEUSUA,NTITUUSUA,COMPETENCIA,RESPONSAVEL,NUMERO,NOME,DOC,CODIGO_SERVICO,DESCRICAO,NOME_PRESTADOR,QUANTIDADE,VALOR_COPARTICIPACAO)
        values (:seq,:num,:numusu,:comp,:respon,:numero,:nome_grande,:doc,:codigo_serv,:descricao,:nome_prest,:qty,:valor_copart)
        """
    conector.executeSQL(sql,[i,231,21,22,List_Nome_prestador[i],40,List_Nome_Usuario[i],List_Numero_Documento[i],83537,Descricao_Procedimento[i],List_Nome_prestador[i],Qtde_Procedimento[i],Valor_Coparticipacao[i]])

    stringResultado = List_Nome_prestador[i] + " " + List_Numero_Documento[i] + " " + List_Nome_Usuario[i] + " " + List_Numero_Doc_Origem[i] + " \n " + List_Data_Validade[i]

    resultado.writelines(stringResultado)

    i = i + 1

#print(List_Nome_prestador[0] + " " + List_Numero_Documento[0] + " " + List_Nome_Usuario[0] + " " + List_Numero_Doc_Origem[0])

#lista tem 1493 elementos
#print(vetorlinha[77])