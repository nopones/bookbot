from stats import count_words,count_characters,sort_on,sorted_list

def get_book_text(path):
    with open (path) as book:
        file_contents = book.read()
        return file_contents

def main():
    path="books/"+"frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    book_text=get_book_text(path)
    words_counted=count_words(book_text)
    print(f"Found {words_counted} total words")
    print("--------- Character Count -------")
    characters_counted=count_characters(book_text)
    characters_list=sorted_list(characters_counted)
    for char_dict in characters_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")
main()
