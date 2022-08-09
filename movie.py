import csv
from re import L, X
from wsgiref.validate import InputWrapper
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
    x = y = 1

    def __init__(self, name, genres, rating):
        self.name = name.lower()
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
        found = False
        for i in range(4):
            for j in range(len(genres_[i])):
                if genre == genres_[i][j]:
                    found = True
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
                    break
            if found:
                break

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

def find_similar(movie_):
    # print(movie_.get_x(), movie_.get_y())
    global movies
    top_ten = [[0,None],[0,None],[0,None],[0,None],[0,None],[0,None],[0,None],[0,None],[0,None],[0,None]]
    for i in range(len(movies)):
        if movies[i].get_name() != movie_.get_name():
            # print(movies[i].get_name()) 
            # print(movies[i].get_x(), movies[i].get_y())
            coeff = recommender.similarity(movies[i].get_x(), movies[i].get_y(), movie_.get_x(), movie_.get_y())
            # print(coeff)
            if coeff > top_ten[0][0]:
                top_ten[0][0] = coeff
                top_ten[0][1] = movies[i].get_name()
        top_ten.sort(key=lambda x: x[0])
    return top_ten

    
    

def main():
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

    inp = input("Enter a movie:")
    check = False
    idx = 0
    while not check:
        for i in range(len(movies)):
            if inp.lower() == movies[i].get_name().lower():
                check = True
                idx = i
        if not check :
            inp = input("That movie does not exist in the database. Please enter another one.")

    top = find_similar(movies[idx])
    for mov in top:
        print(mov[1])
    

if __name__ == "__main__":
    main()



# Note: keep track of euclidean distance 
# and angle to break ties
# Genres: 
# 1) Action/Adventure (+,+)
# 2) Horror/Thriller/Crime/Mystery/Sci-Fi (-,+)
# 3) Drama/History (-,-)
# 4) Comedy/Romance (+,-)