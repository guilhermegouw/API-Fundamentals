from flask import Flask
from flask_restful import Api

from resources.recipe import RecipeListResource, RecipeResource, RecipePublicResource


app = Flask(__name__)
api = Api(app)

api.add_resource(RecipeListResource, "/recipes")
api.add_resource(RecipeResource, "/recipes/<int:recipe_id>")
api.add_resource(RecipePublicResource, "/recipes/<int:recipe_id>/publish")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
