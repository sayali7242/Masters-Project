import pandas as pd 

df=pd.read_csv('ado_5', sep=' ', header=None)
df.columns = ["SNode", "ENode", "Weight"]

df = df.sort_values(by='Weight', ascending=False)

df_5k = df.head(5000)
df_5k.to_csv('ado_5_top_5k', sep=' ', index=False, header=False)

