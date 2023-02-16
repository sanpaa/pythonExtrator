#import xlrd
#arquivo =  xlrd.open_workbook("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\140_Copart 12.2022.xlsx")
#plan =  arquivo.sheet_by_name("Planilha1")
#print(plan.col_values[0])


import openpyxl

arq = openpyxl.load_workbook("C:\\Users\\paulo.sanches\\Desktop\\TestePastinha\\140_Copart 12.2022.xlsx")
sheet = arq.active
ws = arq['Planilha1']
rangevalor = ws['A2':'AA1494']
for v1 in rangevalor:
    print(v1.value)
