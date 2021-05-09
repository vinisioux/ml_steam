import pandas as pd
from pandas_profiling import ProfileReport

df_steam = pd.read_csv('C:\\Users\\sioux\\Documents\\projects\\facul\\estudo_para_ac\\ac\\steam.csv')

relatorio = ProfileReport(df_steam)
relatorio.to_file('C:\\Users\\sioux\\Documents\\projects\\facul\\estudo_para_ac\\ac\\steam_rel.html')
