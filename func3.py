#This project focuse on *args and **kwargs to create a function that takes in any number of arguments and keyword arguments and returns the sum of all the arguments and keyword arguments.

username = input("Enter your name: ")
user_div = input("Enter your division: ")
def explain_args_kwargs(*value_user_arg):

    return value_user_arg

value_user_arg = explain_args_kwargs(username, user_div)   
print(value_user_arg)

#total_args = int(input("Enter the number of arguments you want to pass: "))
#username = input("Enter your name: ")

#user_args = input("Enter the integer arguments you want to pass: ").split()
#while len(user_args) != total_args:
 #   print(f"You have entered {len(user_args)} arguments. Please enter {total_args} arguments.")
   # user_args = input("Enter the integer arguments you want to pass: ").split()