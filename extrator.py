#import pandas as pd
#excel_col = ['Codigo Prestador','Numero Documento','Especie Fatura','Contratante','Numero Fatura','Nome Usuario']
#df = pd.read_excel('C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\140_Copart 12.2022.xlsx')
#print(df['Nome Prestador'])


import pandas as pd
excel_col = ['Unidade Prestador','Codigo Prestador','Nome Prestador','Numero Documento','Numero Doc Origem','Data Realizacao','Numero Fatura','Ano Fatura','Valor Procedimento','Qtde Procedimento','Origem Movimento']



file1 = open("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\teste.txt", mode='w')
df = pd.read_excel('C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\140_Copart 12.2022.xlsx')

for i in df:
    b = i
    b = str(b)
    if b == ('NaN'):
        continue
    else:
        file1.write('\n')
    file1.writelines(b)

file1.close()


    #df.to_excel("output.xlsx")

#print(df[excel_col])







