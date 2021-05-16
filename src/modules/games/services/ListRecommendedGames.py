
def ListRecommendedGames(name):
    
    from main import recommendedGames
   
    recommendedGamesList = recommendedGames(name)

    return recommendedGamesList
