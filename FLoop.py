#This project focuses on the use of for loop to find a word in a paragraph and count its frequency.

user = input("Enter your paragraph: ")

wordfind = input("Enter the word you want to find: ")



for word in user.split():
    if word == wordfind:
        print(f"The word '{wordfind}' was found in the paragraph.The frequency of the word is: {user.split().count(wordfind)}")
        break

else:
    print(f"The word '{wordfind}' was not found in the paragraph.")