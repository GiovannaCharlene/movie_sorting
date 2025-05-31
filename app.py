# Import necessary modules from Flask and Python standard library
from flask import Flask, request, jsonify
import json
import os

# Create a Flask application instance
app = Flask(__name__)

# Define a function to sort a list of dictionaries using multiple keys
def multisort(data, sort_keys):
    # Iterate over the sort keys in reverse order (lowest priority first)
    for key, reverse in reversed(sort_keys):
        # Sort the data in place using the current key and direction
        data.sort(key=lambda x: x[key], reverse=reverse)
    return data

# Define a POST endpoint at /sort
@app.route("/sort", methods=["POST"])
def sort_movies():
    # Read the JSON payload sent by the client
    payload = request.get_json()

    # Extract the list of movies and the desired sort order
    movies = payload.get("movies", [])
    sort_order = payload.get("sort_order", [])

    # Apply the multisort algorithm to the data
    result = multisort(movies, sort_order)

    # Return the sorted result as a JSON response
    return jsonify(result)

@app.route("/demo", methods=["GET"])
def demo_sort():
    # Obtener ruta relativa al archivo movies.json
    json_path = os.path.join(os.path.dirname(__file__), "movies.json")
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            movies = json.load(f)
    except Exception as e:
        return jsonify({"error": f"Error reading movies.json: {str(e)}"}), 500

    # Orden fijo: rating (desc), release_date (asc)
    sort_order = [("rating", True), ("release_date", False)]
    result = multisort(movies, sort_order)
    return jsonify(result)

# Run the Flask development server if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)