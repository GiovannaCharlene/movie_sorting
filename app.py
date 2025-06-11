# Import necessary modules from Flask and Python standard library
from flask import Flask, request, jsonify
import json
import os

# Import sorting logic from separate module
from sorting_utils import multisort

# Create a Flask application instance
app = Flask(__name__)

# Define a POST endpoint at /sort
@app.route("/sort", methods=["POST"])
def sort_movies():
    try:
        payload = request.get_json(force=True)

        if not isinstance(payload, dict):
            return jsonify({"error": "Invalid JSON structure."}), 400

        movies = payload.get("movies")
        sort_order = payload.get("sort_order")

        if not isinstance(movies, list) or not isinstance(sort_order, list):
            return jsonify({"error": "Invalid input: 'movies' and 'sort_order' must be lists."}), 400

        for item in sort_order:
            if not (isinstance(item, list) and len(item) == 2 and isinstance(item[0], str) and isinstance(item[1], bool)):
                return jsonify({"error": "Each sort_order entry must be [string, boolean]."}), 400

        result = multisort(movies, sort_order)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# Define a GET endpoint at /demo
@app.route("/demo", methods=["GET"])
def demo_sort():
    json_path = os.path.join(os.path.dirname(__file__), "movies.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return jsonify({"error": f"Error reading movies.json: {str(e)}"}), 500

    movies = data.get("movies", [])
    sort_order = [("rating", True), ("release_date", False)]
    try:
        result = multisort(movies, sort_order)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Error sorting demo data: {str(e)}"}), 500

# Run the Flask development server if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)