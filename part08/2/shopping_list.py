class Book:
    def __init__(self, name: str,author: str, genre: str ,year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
print(python.author)
        