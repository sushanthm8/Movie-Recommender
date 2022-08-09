import pandas as pd
import numpy as np
import csv


movies = []
with open("data/MovieGenre.csv", 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        name = ""
        rating = ""
        genres = []
        for col in range(len(row)):
            if col == 2:
                name = row[col]
            elif col == 3:
                rating = row[col]
            elif col == 4:
                genres = row[col].split('|')
        print(name, rating, genres)



 