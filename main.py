import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df_steam = pd.read_csv('C:\\Users\\sioux\\Documents\\projects\\facul\\estudo_para_ac\\ac\\steam.csv')

#relatorio = ProfileReport(df_steam)
#relatorio.to_file('C:\\Users\\sioux\\Documents\\projects\\facul\\estudo_para_ac\\ac\\steam_rel.html')

newCategory = 'Single-Player'
newGenre = 'Action'
newTags = 'FPS'

# Feature alvo
df_steam['alvo'] = df_steam['name'] 

# Tratamento de dados qualitativos

categories = []

splitCategories = lambda x: categories.append(x.split(';'))

df_steam['categories'].apply(splitCategories)


flat_list = [item for sublist in categories for item in sublist]

listCategories = set(flat_list)

for i in listCategories:
    df_steam[i] = 0


#def teste(x):
    
    

categoryExists = lambda x: 1 if(newCategory.lower() in x.lower()) else 0
df_steam['pre_categories'] = df_steam['categories'].apply(categoryExists)

genreExists = lambda x: 1 if(newGenre.lower() in x.lower()) else 0
df_steam['pre_genre'] = df_steam['genres'].apply(genreExists)

tagsExists = lambda x: 1 if(newTags.lower() in x.lower()) else 0
df_steam['pre_steamspy_tags'] = df_steam['steamspy_tags'].apply(tagsExists)


df_final = df_steam[[
'alvo',
'pre_categories',
'pre_genre',
'pre_steamspy_tags',
]]

# Demonstrar correlacoes

df_steam.corr()

# Separar dados Treino e Teste

y = df_final['alvo']
X = df_final[['pre_categories',
'pre_genre',
'pre_steamspy_tags']].values

# knn

nbrs = NearestNeighbors(n_neighbors=7, algorithm='ball_tree').fit(X)
distancias, indices = nbrs.kneighbors(X)

game = 8000

print(X[game])
print(distancias[game])
print(indices[game])
print('media distancia: ', np.mean(distancias))
print('mediana distancia: ', np.median(distancias))

y_parecidos = []

for parecido in indices[game]:
    print(parecido, ' : ', y[parecido])
    if(parecido != game):
        y_parecidos.append(y[parecido])
    
#print('vai pagar? ', np.bincount(y_parecidos).argmax())


