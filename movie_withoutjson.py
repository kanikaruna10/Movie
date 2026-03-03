import json

movie_database = {}

def add_movie():
    title = input("Enter the movie title: ")
    genre = input("Enter the movie genre: ")
    director = input("Enter the name of the director: ")
    release_date = input("Enter the release date of the movie (YYYY-MM-DD): ")
    actors = input("Enter the names of the actors (separated by commas): ")
    actors_list = [a.strip() for a in actors.split(",")]  # FIX 1: strip whitespace

    movie_database[title] = {
        "genre": genre,
        "director": director,
        "release_date": release_date,
        "actors": actors_list
    }
    print(f"{title} has been added to the database.")

def view_all_movies():
    if not movie_database:
        print("No movies in the database.")
        return
    print("All movies in the database:\n")
    for movie, info in movie_database.items():
        print(f"Movie: {movie}")
        for key, value in info.items():
            print(f"  {key}: {value}")
        print()

def edit_movie():
    title = input("Enter the movie title to edit: ")
    if title in movie_database:
        print(f"Current information for {title}:")
        for key, value in movie_database[title].items():  # FIX 2: only show selected movie
            print(f"  {key}: {value}")

        genre = input("Enter the movie genre (or press Enter to keep current): ")
        director = input("Enter the director name (or press Enter to keep current): ")
        release_date = input("Enter the release date YYYY-MM-DD (or press Enter to keep current): ")
        actors = input("Enter actor names separated by commas (or press Enter to keep current): ")

        if genre:
            movie_database[title]["genre"] = genre
        if director:
            movie_database[title]["director"] = director
        if release_date:
            movie_database[title]["release_date"] = release_date
        if actors:
            movie_database[title]["actors"] = [a.strip() for a in actors.split(",")]  # FIX 1

        print(f"{title} has been updated.")
    else:
        print(f"{title} is not in the database.")

def delete_movie():
    title = input("Enter the movie title to delete: ")
    if title in movie_database:
        del movie_database[title]
        print(f"{title} has been deleted from the database.")
    else:
        print(f"{title} is not in the database.")

def search_movies():
    print("Search movies in the database:")
    criteria = input("Enter the search criteria: ").lower()
    matches = []
    for movie, info in movie_database.items():
        # FIX 3: search actors properly using any()
        actor_match = any(criteria in actor.lower() for actor in info["actors"])
        if (criteria in movie.lower() or
                criteria in info["genre"].lower() or
                criteria in info["director"].lower() or
                actor_match):
            matches.append(movie)

    if matches:
        print("Matches found:")
        for match in matches:
            print(f"\n  Movie: {match}")
            for key, value in movie_database[match].items():
                print(f"  {key}: {value}")
    else:
        print("No matches found.")

while True:
    print("\n====Movie Database Management System====")
    print("1. Add a new movie")
    print("2. Edit an existing movie")
    print("3. Delete a movie")
    print("4. View all movies")
    print("5. Search movies")
    print("6. Exit")
    user_choice = input("Please enter your choice: ")

    if user_choice == "1":
        add_movie()
    elif user_choice == "2":
        edit_movie()
    elif user_choice == "3":
        delete_movie()
    elif user_choice == "4":
        view_all_movies()
    elif user_choice == "5":
        search_movies()
    elif user_choice == "6":
        exit()
    else:
        print("Invalid choice. Please try again.")