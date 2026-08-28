"""This funtion uses .split method to convert a paragraph into a list of words and then uses for loop to iterate through the list to find the word and count its frequency."""
#This project is a simple word deletion program that takes a paragraph and a word as input and deletes the word from the paragraph if it is found.
def del_word(word_to_delete, paragraph):
    
    paragraph = paragraph.replace(word_to_delete, "")
    return paragraph

user_input = input("Enter your paragraph: ")
word_to_delete = input("Enter the word you want to delete: ")

for word in user_input.split():
    if word == word_to_delete:
        print(f"The word '{word_to_delete}' was found in the paragraph {user_input.split().count(word_to_delete)} times.")
        print(f"The word '{word_to_delete}' was found in the paragraph and has been deleted.")
        print(f"The updated paragraph is: {del_word(word_to_delete, user_input)}")

else:
    print(f"The word '{word_to_delete}' was not found in the paragraph.")