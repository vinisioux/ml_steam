from flask import jsonify, request
from server import app
from response import Response

@app.route("/games", methods=["GET"])
def FindGame():
    try:
      from modules.games.services.ListRecommendedGames import ListRecommendedGames
      gameName = request.args.get('gameName')

      recommendedGamesList = ListRecommendedGames(gameName)
      
      Response["data"] = {"games": recommendedGamesList}
      Response["status"] = 200
      Response["message"] = "success"

      return jsonify(Response)
    except AssertionError as error:
      print(error)
      Response["data"] = ""
      Response["status"] = 400
      Response["message"] = "failed"

      return jsonify(Response)
