import pandas as pd

# ? configurando una variable con informacion de una hoja de excel

df = pd.read_excel("lista.xlsx")
print(df.head(10))
print(df)
