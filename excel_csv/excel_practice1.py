import pandas as pd 


workbook1 = "file1.xlsx"
workbook2 = "file2.xlsx"

df_1 = pd.read_excel(workbook1)
df_2 = pd.read_excel(workbook2)

#print(df_1.columns)
#print(df_2.columns)
df_3 = pd.merge(df_1, df_2, on='name')
#print(df_3)
df_3.to_excel("merged_workbooks.xlsx")