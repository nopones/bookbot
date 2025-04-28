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

def sort_on(dict):
    return dict["num"]

def sorted_list(dict):
    list_dict=[]
    for char,count in dict.items():
        list_dict.append({"char":char,"num":count})
    list_dict.sort(reverse=True,key=sort_on)
    return list_dict

#For Testing

#path="books/"+"frankenstein.txt"
#with open (path) as book:
#    file_contents = book.read()

#test=count_characters(file_contents)
#print(test)
#result=sorted_list(test)
#print(result)


