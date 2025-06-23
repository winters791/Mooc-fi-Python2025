class Book:
    def __init__(self,Title: str,Author: str,Genre: str,Date: int):
        self.Title = Title
        self.Author = Author
        self.Genre = Genre
        self.Date = Date

def older_book(book1: Book, book2: Book):
    if book1.Date > book2.Date:
        print(f"{book2.Title} is older, it was Published in {book2.Date} ")
    elif book1.Date < book2.Date:
        print(f"{book1.Title} is older, it was Published in {book1.Date} ")
    else:
        print("Same Age")

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)
