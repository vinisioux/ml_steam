import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
from sklearn.neighbors import NearestNeighbors

df_steam = pd.read_csv('C:\\Users\\sioux\\Documents\\projects\\facul\\estudo_para_ac\\ac\\steam.csv')

#relatorio = ProfileReport(df_steam)
#relatorio.to_file('C:\\Users\\sioux\\Documents\\projects\\facul\\estudo_para_ac\\ac\\steam_rel.html')

newCategory = 'Single-Player'

#categoryExists = lambda x: 18 if(np.isnan(x) or x < 18) else x
categoryExists = lambda x: 1 if(newCategory.lower() in x.lower()) else 0
df_steam['pre_categories'] = df_steam['categories'].apply(categoryExists)