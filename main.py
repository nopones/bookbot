
def get_book_text(path):
    with open (path) as book:
        file_contents = book.read()
        return file_contents

def count_words(string):
    list_of_words=string.split()
    words= len(list_of_words)
    return (words)

def main():
    path="books/"+"frankenstein.txt"
    book_text=get_book_text(path)
    words_counted=count_words(book_text)
    print(f"{words_counted} words found in the document")

main()
