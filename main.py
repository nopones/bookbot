from stats import count_words,count_characters

def get_book_text(path):
    with open (path) as book:
        file_contents = book.read()
        return file_contents

def main():
    path="books/"+"frankenstein.txt"
    book_text=get_book_text(path)
    words_counted=count_words(book_text)
    characters_counted=count_characters(book_text)
    print(f"{words_counted} words found in the document")
    print (characters_counted)

main()
