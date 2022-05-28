
class Book:
    def __init__(self, title = '', author = '', year = 0):
        self.title = title
        self.author = author
        self.year = year
    def get_book(self):
        print(f'title={self.title} author={self.author} year={self.year}')


def GetByAuthor(author, books): #Get title and year of books by this author made later than 1960
    for a in books:
        if a.author == author and int(a.year) >= 1960:
            print(f'Title: {a.title}, Year: {a.year}')

def GetByName(name, books):  #Get authors and year of books with this title
    for a in books:
        if a.title == name:
            print(f'Year: {a.year}, Author: {a.author}')

def main():
    lines = []
    with open('books.txt') as f: #Reading file
        lines = f.readlines()
    books = []
    for l in lines: #Creating books objects
        words = l.split()
        books.append(Book(title=words[0], author=words[1], year=words[2]))
    foo = input('Enter NAME or AUTHOR\n')
    arg = input('Enter argument\n')
    if foo == 'NAME':
        GetByName(arg, books)
    if foo == 'AUTHOR':
        GetByAuthor(arg, books)
    

if __name__ == "__main__":
    main()