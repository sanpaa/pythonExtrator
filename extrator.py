import pandas as pd

df = pd.read_excel('C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\140_Copart 12.2022.xlsx', None)

print(df)

def extrairdadosexcel(nomeentrada,nomesaida):
    file1 = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\"+nomesaida+".txt", 'w+')

    for i in df["Planilha1"][nomeentrada]:
        b = i
        b = str(b)
        print(b)
        if b == 'NaN' or b == 'nan' or b == 'Nan':
            continue
        else:
            file1.write('\n')
        file1.writelines(b)
    file1.close()

# Nome Prestador -X- Numero Documento -X- Nome Usuario -X- Numero Doc Origem -X- Data Realizacao -X- Data Realizacao,
# Cod Procedimento,Descricao Procedimento,Contratante,Qtde Procedimento,Valor Coparticipacao,
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
