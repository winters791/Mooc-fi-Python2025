class Series:
    def __init__(self, Title: str, Seasons: int, Genres: list):
        self.Title = Title
        self.Seasons = Seasons
        self.Genres = ",".join(Genres)
        self.counter = 0
        self.rating = 0
    def rate(self,Rating: int):
        self.counter += 1
        self.rating += Rating
        self.average_rating = round(self.rating/self.counter,2)

    def __str__(self):
        return(f"{self.Title}({self.Seasons} seasons)\ngenres: {self.Genres}\n{self.counter} ratings,average {self.average_rating} points")


dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)
