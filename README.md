# Multisorting Algorithm

## Overview

This project implements a Flask API that sorts a list of movies by multiple criteria using a custom Python multisort function.  
You can sort by any combination of fields such as rating, release date, title, etc.

## How to Run

1. Clone the repository or download the zip:

```bash
git clone https://github.com/GiovannaCharlene/movie_sorting.git
cd movie_sorting
```

2. **(Optional but recommended) Create a virtual environment:**

### On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### On Windows CMD:

```cmd
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Flask app:

```bash
python app.py
```

The app will start a development server at http://127.0.0.1:5000.

## Usage

There are two ways to use this API:

### 1. Quick demo with fixed data

Open your browser or send a GET request to:  
`http://127.0.0.1:5000/demo`  

This endpoint reads the `movies.json` file in the project and returns the movies sorted by:

- `rating` (descending)  
- `release_date` (ascending)

### 2. Custom sorting with POST

Send a POST request to `/sort` with a JSON payload including your own movies list and sort order.

Example JSON payload:

```json
{
  "movies": [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "release_date": "2010-07-16"},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2, "release_date": "1972-03-24"}
  ],
  "sort_order": [["rating", true], ["release_date", false]]
}
```

The API will respond with the sorted list based on your criteria.

## Sample Output from `/demo` or `/sort`

```
{'title': 'The Godfather', 'genre': 'Crime', 'rating': 9.2, 'release_date': '1972-03-24'}
{'title': 'Inception', 'genre': 'Sci-Fi', 'rating': 8.8, 'release_date': '2010-07-16'}
{'title': 'The Matrix', 'genre': 'Sci-Fi', 'rating': 8.7, 'release_date': '1999-03-31'}
{'title': 'Interstellar', 'genre': 'Adventure', 'rating': 8.6, 'release_date': '2014-11-07'}
{'title': 'Parasite', 'genre': 'Drama', 'rating': 8.6, 'release_date': '2019-05-30'}
```

## Author

Giovanna Charlene Chichía Cerda