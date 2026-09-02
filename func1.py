#This project focuses on creating, using and calling a function
import random
"""This function measures the strength of a passcode based on its length. A passcode is considered strong if it has 8 or more characters, and weak if it has less than 8 characters."""
def keyword_len():
    return "the length of passcode is {}".format(len(pass_input))

"""This function randomly generates a passcode and measures its strength based on its length.It suggests a stronger passcode if length of passcode is less than 8."""
def multi_keyword_strength():
    randomcode = random.randint(10000000, 999999999)
    return randomcode

print("Welcome to the passcode strength checker!")
pass_input = input("Please enter your passcode: ")

if len(pass_input) < 8:
        print("Passcode is weak.")
        print(keyword_len())
        print("Here is a randomly generated passcode for you:{}".format(multi_keyword_strength()))
else:
        print("Passcode is strong.")
        print(keyword_len())