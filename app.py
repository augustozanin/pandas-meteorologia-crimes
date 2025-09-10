import pandas as pd

df_dados_criminais_2021 = pd.read_csv('dados_criminais/dados_criminais_2021.csv', delimiter=';' ,encoding="iso-8859-1")
print(df_dados_criminais_2021.head())

print('teste')