import pandas as pd
from sklearn.neighbors import NearestNeighbors
import json

df_steam = pd.read_csv('C:\\Users\\sioux\\Documents\\projects\\facul\\estudo_para_ac\\ac\\steam.csv')
df_steam.drop(['english', 'release_date', 'developer', 'publisher', 'platforms', 'required_age', 'achievements', 'average_playtime', 'median_playtime', 'owners', 'price'], axis=1, inplace=True)

# Tratamento de dados qualitativos

# categories
categories = []
df_steam['categories'].apply(lambda x: categories.append(x.split(';')))
flat_list = [item for sublist in categories for item in sublist]

listCategories = list(set(flat_list))

dados_categoria = {}
for categoria in listCategories:
    dados_categoria[categoria] = []

def cria_categoria(categorias):
    for categoria in listCategories:
        if(categoria in categorias):
            dados_categoria[categoria].append(1)
        else:
            dados_categoria[categoria].append(0)
    
df_steam['categories'].apply(cria_categoria)

df_categories = pd.DataFrame(dados_categoria, columns=listCategories)

df_steam = pd.concat([df_steam, df_categories], axis=1, join='inner')

## categories
##################################################
# genres

genres = []
df_steam['genres'].apply(lambda x: genres.append(x.split(';')))
flat_list = [item for sublist in genres for item in sublist]

listGenres = list(set(flat_list))

dados_genre = {}
for genre in listGenres:
    dados_genre[genre] = []

def cria_genre(genres):
    for genre in listGenres:
        if(genre in genres):
            dados_genre[genre].append(1)
        else:
            dados_genre[genre].append(0)
    
df_steam['genres'].apply(cria_genre)

df_genres = pd.DataFrame(dados_genre, columns=listGenres)

df_steam = pd.concat([df_steam, df_genres], axis=1, join='inner')

## genres
##################################################
# tags
tags = []
df_steam['steamspy_tags'].apply(lambda x: tags.append(x.split(';')))
flat_list = [item for sublist in tags for item in sublist]

listTags = list(set(flat_list))

dados_tags = {}
for tag in listTags:
    dados_tags[tag] = []

def cria_tag(tags):
    for tag in listTags:
        if(tag in tags):
            dados_tags[tag].append(1)
        else:
            dados_tags[tag].append(0)
    
df_steam['steamspy_tags'].apply(cria_tag)

df_tags = pd.DataFrame(dados_tags, columns=listTags)

df_steam = pd.concat([df_steam, df_tags], axis=1, join='inner')

## tags
##################################################
   

df_final = df_steam[df_steam.columns.difference([
    'appid',
    'name', 
    'categories', 
    'genres', 
    'steamspy_tags', 
    'positive_ratings', 
    'negative_ratings'
])]


# KNN

X = df_final.values

nbrs = NearestNeighbors(n_neighbors=11, algorithm='ball_tree').fit(X)
distancias, indices = nbrs.kneighbors(X)

def returnGameIndex(name):
    for i, row in df_steam.iterrows():
        if (name.lower() == row['name'].lower()):
            return i
    else:
        return 'Jogo nao encontrado'
    
game = returnGameIndex('among us')

print(game)

games_parecidos = []

for parecido in indices[game]:
       
    newGame = {
        'name': df_steam.iloc[parecido]['name'],
        'categories': df_steam.iloc[parecido]['categories'],
        'genres': df_steam.iloc[parecido]['genres'],
        'steamspy_tags': df_steam.iloc[parecido]['steamspy_tags'],
        'positive_ratings': int(df_steam.iloc[parecido]['positive_ratings']),
        'negative_ratings': int(df_steam.iloc[parecido]['negative_ratings'])
    }
    
    convertNewGameToJson = json.dumps(newGame)
    loadNewGameJson = json.loads(convertNewGameToJson)
    
    if(parecido != game):
        games_parecidos.append(loadNewGameJson)
    
print(games_parecidos)
