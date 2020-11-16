import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):
    
    # Load the raw data
    animedf = pd.read_csv(url_or_path_to_csv_file)
    
    # Remove any Missing or Unknown values as well as the anime_id column
    animedf = animedf.drop(
        labels = ['anime_id'], axis = 1
        ).dropna(
        subset = ['genre', 'type', 'episodes', 'rating', 'name']
        ).loc[
        lambda row: ~row['episodes'].str.contains('Unknown')
    ]
    
    return animedf

def means_of_genres(df):
    genredf = df.copy()
    # Gropu genres together, take the mean, and sort by rating
    split_column(genredf).groupby(
        'genre'
    ).mean(
    ).sort_values(
        by = ['rating'], ascending = False
    ).reset_index()
    
    return genredf

def split_column(df):
    genredf = df.copy()
    # Transform the strings of genres into lists
    genredf['genre'] = genredf['genre'].transform(
        lambda x: x.split(', ')
    )

    # Split the lists into individual rows
    genredf = genredf.explode(
        column = 'genre'
    )
    
    return genredf