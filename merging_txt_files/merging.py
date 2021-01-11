#Check this video: https://www.youtube.com/watch?v=cRELNmDpaks&list=PLCN-JplaYuP4gDPNweg-bbGwNL36A3Hog&index=2&t=0s

import pandas as pd
#import numpy as np

id_file = "contigs_ids.txt"
data_file = "contigs_DE.txt"
#output_file = "annotated_DE.txt"

#df_id = pd.read_fwf(id_file, sep=r'\t')
#df_data = pd.read_fwf(data_file, sep=r'\t')

df_id = pd.read_csv(id_file, sep=r"\t", engine="python")
df_data = pd.read_csv(data_file, sep=r"\t", engine="python")
#print(df_id.head())
#print("\n", df_data.head())

merge = pd.merge(df_data, df_id, on="contig", how="left")
print(merge.tail())

merge.to_csv(r'merged_DE.txt', sep='\t', mode='a')

