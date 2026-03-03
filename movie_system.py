# Define dictionary of movies and their information
movies = {
    "The Dark Knight": {
        "year": 2008,
        "genre": "Action",
        "director": "Christopher Nolan",
        "actors": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]
    },
    "Inception": {
        "year": 2010,
        "genre": "Sci-Fi",
        "director": "Christopher Nolan",
        "actors": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]
    },
    "Pulp Fiction": {
        "year": 1994,
        "genre": "Crime",
        "director": "Quentin Tarantino",
        "actors": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"]
    }
}

# Print out the movies and their information using square bracket syntax and .keys and .values
for movie in movies:
    print(f"Movie: {movie}")
    for key, value in movies[movie].items():
        print(f"{key}: {value}")
    print()

# Update an element in the dictionary
movies["The Dark Knight"]["year"] = 2009

# Delete an element from the dictionary
del movies["Pulp Fiction"]

# Get a value from the dictionary using .get
genre = movies.get("Inception").get("genre")
print(f"The genre of Inception is {genre}.")
