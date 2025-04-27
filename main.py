
def get_book_text(path):
    with open (path) as book:
        file_contents = book.read()
        print (file_contents)

def main():
    path="books/"+"frankenstein.txt"
    get_book_text(path)

main()
