import pandas as pd
df_1 = pd.read_csv("file1.csv")
df_2 = pd.read_csv("file2.csv")

#print(df_1)
merge = pd.merge(df_1, df_2, on="name")
merge.to_csv("merged.csv")