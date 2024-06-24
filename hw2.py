class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year

    def get_publisher(self):
        return self.publisher
    
    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_genre(self):
        return self.genre
    
    def set_genre(self, genre):
        self.genre = genre

    def get_author(self):
        return self.author
    
    def set_author(self, author):
        self.author = author

    def get_price(self):
        return self.price
    
    def set_price(self, price):
        self.price = price



book = Book("1984", 1949, "sd", "as", "dd", 19.99)

print(f"Title: {book.get_title()}")
print(f"Year: {book.get_year()}")
print(f"Publisher: {book.get_publisher()}")
print(f"Genre: {book.get_genre()}")
print(f"Author: {book.get_author()}")
print(f"Price: ${book.get_price()}")


book.set_title("Adm")
book.set_year(1945)
book.set_publisher("sddssd")
book.set_genre("asd")
book.set_author("aaal")
book.set_price(14.99)

print("\nUpdated book data:\n")
print(f"Title: {book.get_title()}")
print(f"Year: {book.get_year()}")
print(f"Publisher: {book.get_publisher()}")
print(f"Genre: {book.get_genre()}")
print(f"Author: {book.get_author()}")
print(f"Price: ${book.get_price()}")
