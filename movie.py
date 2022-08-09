# from data import Data
import csv
from re import L, X
import recommender

genres_ = [
["action", "adventure"],
["horror", "thriller", "crime", "mystery", "sci-fi"],
["drama", "history"],
["comedy", "romance"]
]

movies = []

class Movie:
    global genres_
    #vector 
    x = y = 1

    def __init__(self, name, genres, rating):
        self.name = name
        self.genres = genres
        self.rating = rating
    
    def get_name(self):
        return self.name
    
    def get_genres(self):
        return self.genres

    def get_rating(self):
        return self.rating

    def make_vector(self):
        genre = self.genres[0].lower()
        # print(genre)
        found = False
        for i in range(4):
            for j in range(len(genres_[i])):
                if genre == genres_[i][j]:
                    found = True
                    # print(i)
                    if i == 0:
                        self.x = self.y = float(self.rating)
                    elif i == 1:
                        self.x = -float(self.rating)
                        self.y = float(self.rating)
                    elif i == 2:
                        self.x = self.y = -float(self.rating)
                    else:
                        self.x = float(self.rating)
                        self.y = -float(self.rating)
                    # category_no = i
                    break
            if found:
                break
            # print(genres_[i][j])
            # print(genres_[i])
            # for j in genres_[i]:
            #     if genre == genres_[j]:
            #         found = True
            #         category_no = i
            #         break
            # if found:
            #     break

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    

def main():
    # f = open("data.txt", "r")
    # for line in f:
        # print(line)
        # tmp = line.split()
        # movies.append(Movie())
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
            found = False
            for genre_type in genres_:
                for genre in genre_type:
                    if genres[0].lower() == genre:
                        found = True
            if found :
                movies.append(Movie(name,genres,rating))

    for movie in movies:
        movie.make_vector()
        # print(movie.get_x(), movie.get_y())

    # print(movies[len(movies)-1].get_name(), movies[len(movies)-1].get_x(), movies[len(movies)-1].get_y())


if __name__ == "__main__":
    main()



# Note: keep track of euclidean distance 
# and angle to break ties
# Genres: 
# 1) Action/Adventure (+,+)
# 2) Horror/Thriller/Crime/Mystery/Sci-Fi (-,+)
# 3) Drama/History (-,-)
# 4) Comedy/Romance (+,-)