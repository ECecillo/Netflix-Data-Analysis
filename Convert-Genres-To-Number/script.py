import pandas as pd
import ast

def load_and_convert_genres(file_path):
    # Charger les données
    data = pd.read_csv(file_path)

    # Convertir les chaînes de genre en listes
    data['genres'] = data['genres'].apply(ast.literal_eval)

    # Extraire tous les genres uniques
    unique_genres = set()
    for genres in data['genres']:
        unique_genres.update(genres)

    # Créer un dictionnaire pour mapper les genres en entiers
    genre_to_int = {genre: i for i, genre in enumerate(unique_genres)}

    # Convertir les genres de chaque entrée en tableau d'entiers
    data['genre_integers'] = data['genres'].apply(lambda genres: [genre_to_int[genre] for genre in genres])

    return data
