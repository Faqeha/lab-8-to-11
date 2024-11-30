class Document:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print("Title:", self.title)
        print("Author:", self.author)

class Book(Document):
    def __init__(self, title, author, genre=None, pages=None):
        Document.__init__(self, title, author)
        self.genre = genre
        self.pages = pages

    def display_info(self):
        Document.display_info(self)
        if self.genre:
            print("Genre:", self.genre)
        if self.pages:
            print("Pages:", self.pages)

class Article(Document):
    def __init__(self, title, author, journal=None, doi=None):
        Document.__init__(self, title, author)
        self.journal = journal
        self.doi = doi

    def display_info(self):
        Document.display_info(self)
        if self.journal:
            print("Journal:", self.journal)
        if self.doi:
            print("DOI:", self.doi)

def save_books_to_file(file_name, books):
    with open(file_name, "w") as file:
        for book in books:
            file.write(book.title + "," + book.author + "," +
                       (book.genre if book.genre else "") + "," +
                       (str(book.pages) if book.pages else "") + "\n")

def save_articles_to_file(file_name, articles):
    with open(file_name, "w") as file:
        for article in articles:
            file.write(article.title + "," + article.author + "," +
                       (article.journal if article.journal else "") + "," +
                       (article.doi if article.doi else "") + "\n")

def read_books_from_file(file_name):
    books = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                title, author, genre, pages = data[0], data[1], data[2] or None, int(data[3]) if data[3] else None
                books.append(Book(title, author, genre, pages))
    except FileNotFoundError:
        print("No books found.")
    return books

def read_articles_from_file(file_name):
    articles = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(",")
                title, author, journal, doi = data[0], data[1], data[2] or None, data[3] or None
                articles.append(Article(title, author, journal, doi))
    except FileNotFoundError:
        print("No articles found.")
    return articles

books = read_books_from_file("books.txt")
articles = read_articles_from_file("articles.txt")

while True:
    print("\nMenu:")
    print("1. Add Book")
    print("2. Add Article")
    print("3. Display Books")
    print("4. Display Articles")
    print("5. Save and Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter title: ")
        author = input("Enter author: ")
        genre = input("Enter genre (or leave blank): ")
        pages = input("Enter number of pages (or leave blank): ")
        books.append(Book(title, author, genre, int(pages) if pages else None))
        print("Book added successfully!")
    elif choice == "2":
        title = input("Enter title: ")
        author = input("Enter author: ")
        journal = input("Enter journal (or leave blank): ")
        doi = input("Enter DOI (or leave blank): ")
        articles.append(Article(title, author, journal, doi))
        print("Article added successfully!")
    elif choice == "3":
        for book in books:
            book.display_info()
            print()
    elif choice == "4":
        for article in articles:
            article.display_info()
            print()
    elif choice == "5":
        save_books_to_file("books.txt", books)
        save_articles_to_file("articles.txt", articles)
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
