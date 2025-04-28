def count_words(string):
    list_of_words=string.split()
    words= len(list_of_words)
    return (words)

def count_characters(string):
    counted_characters={}
    lowercase_text=string.lower()
    for char in lowercase_text:
        #print (char)
        if char in counted_characters:
            counted_characters[char] += 1  # Increment the existing count
        else:
            counted_characters[char] = 1
    return counted_characters

