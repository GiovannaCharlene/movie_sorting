# Multisorting Algorithm API

## Overview

This project implements a Flask API that sorts a list of movies by multiple criteria using a custom Python `multisort()` function.  
The codebase is modular, separating logic into reusable components, and includes input validation and error handling for robust and maintainable behavior.

You can sort by any combination of fields such as `rating`, `release_date`, `title`, etc.

## Key Features

- ✅ **Modular structure**: Sorting logic lives in a separate `sorting_utils.py` file for reusability.
- 🛡️ **Input validation**: Ensures that input JSON has the correct format, with clear error messages.
- 🚫 **Error handling**: Returns proper HTTP status codes (400/500) for invalid or malformed input.
- 🔁 **Multisorting**: Supports cascading sort order by multiple fields with ascending or descending control.

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

The app will start a development server at:  
📍 `http://127.0.0.1:5000`

---

## Usage

There are two ways to use this API:

### 1. 🔎 Quick demo with predefined data

Open your browser or send a GET request to:

```
http://127.0.0.1:5000/demo
```

This endpoint reads the `movies.json` file and returns the movies sorted by:

- `rating` (descending)
- `release_date` (ascending)

### 2. 📬 Custom sorting with POST

Send a POST request to `/sort` with your own movie data and sorting rules.

#### Example JSON Payload:

```json
{
  "movies": [
    { "title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "release_date": "2010-07-16" },
    { "title": "The Godfather", "genre": "Crime", "rating": 9.2, "release_date": "1972-03-24" }
  ],
  "sort_order": [
    ["rating", true],
    ["release_date", false]
  ]
}
```

#### Example Invalid Input (triggers error handling):

```json
{
  "movies": "not a list",
  "sort_order": { "rating": true }
}
```

✅ The API will return a clear error message and status code `400`.

---

## Sample Output from `/demo` or `/sort`

```
{'title': 'The Godfather', 'genre': 'Crime', 'rating': 9.2, 'release_date': '1972-03-24'}
{'title': 'Inception', 'genre': 'Sci-Fi', 'rating': 8.8, 'release_date': '2010-07-16'}
{'title': 'The Matrix', 'genre': 'Sci-Fi', 'rating': 8.7, 'release_date': '1999-03-31'}
{'title': 'Interstellar', 'genre': 'Adventure', 'rating': 8.6, 'release_date': '2014-11-07'}
{'title': 'Parasite', 'genre': 'Drama', 'rating': 8.6, 'release_date': '2019-05-30'}
```

---

## File Structure

```
movie_sorting_api/
├── app.py              # Main Flask app with endpoints
├── sorting_utils.py    # Contains the multisort() function
├── movies.json         # Example data file
├── README.md           # This file
└── requirements.txt    # Flask dependency
```

---

## Author

Giovanna Charlene Chichía Cerda