import json
from flask import Flask, jsonify, request
from http import HTTPStatus


app = Flask(__name__)

recipes = [
    {
        "id": 1,
        "name": "Egg Salad",
        "description": "This is a lovely egg salad recipe.",
    },
    {
        "id": 2,
        "name": "Tomato Pasta",
        "description": "This is a lovely tomato pasta recipe.",
    },
]


@app.route("/recipes", methods=["POST"])
def create_recipe():
    data = request.get_json()
    name = data.get("name")
    description = data.get("description")

    recipe = {"id": recipes[-1]["id"] + 1, "name": name, "description": description}

    recipes.append(recipe)

    return jsonify(recipe), HTTPStatus.CREATED


@app.route("/recipes", methods=["GET"])
def get_recipes():
    return jsonify({"data": recipes})


@app.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe:
        return jsonify(recipe)
    return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND


@app.route("/recipes/<int:recipe_id>", methods=["PUT"])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if not recipe:
        return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND

    data = request.get_json()
    recipe.update({"name": data.get("name"), "description": data.get("description")})
    return jsonify(recipe)


@app.route("/recipes/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe:
        recipes.remove(recipe)
        return "", HTTPStatus.NO_CONTENT
    return jsonify({"message": "recipe not found"}), HTTPStatus.NOT_FOUND


if __name__ == "__main__":
    app.run()
