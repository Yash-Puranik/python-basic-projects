#This is a console based ATM & Bank Account Simulator that incorporates...... many concepts :))
#Hi there!

def git_temp():
    print("This is a temporary function to test git commands. Please ignore this function.")
    
def user_database(user_name, user_balance):
    return user_name, user_balance

def user_access(chk_balance, depo_balance, withdraw_amt):
    chk_balance = user_balance
    depo_balance = user_depo_balance
    withdraw_amt = user_withdraw_amt
    return f"check balance: {chk_balance}, deposit balance: {depo_balance}, withdraw amount: {withdraw_amt}"


print(f"Welcome to the ATM & Bank Account Simulator! Please enter your details to create an account.")


user_name = input("Please Enter your name: ")
user_pin = input("Please Enter your 4 digit pin: ")

for attempt in range(1, 4):
    
    while True:
        if len(str(user_pin)) == 4:
            print(f"Your pin is valid. You can now access your account.")
            print(f"Thank you {user_name} for joining with us. Your account has been created successfully. You can now access your account using your pin.")
            user_balance = float(input("Please Enter your account balance: "))
            print(f"Your current balance is {user_balance}.")
            db = user_database(user_name, user_balance)
            print(db)
            break
        elif len(str(user_pin)) != 4:
            print(f"Your pin is incorrect. Please enter a 4 digit pin.")
            if attempt < 3:
                user_pin = input("Please Enter your 4 digit pin: ")
            break
    if len(str(user_pin)) == 4:
        break
    print(f"Please enter your 4 digit pin to access your account. You have {3-attempt} attempts left.")
else:
    print(f"You have exceeded the maximum number of attempts. Please try again later.")    

access = print("Please enter access activity you would like to use: \n1. Deposit Money \n2. Withdraw Money \n3. Exit")


if access == 1:
    print(f"Your current balance is {user_balance}.")
    user_depo_balance = float(input("Please Enter your deposit amount: "))
    total_balance = user_balance + user_depo_balance
    print(f"Your total balance after deposit is {total_balance}.")

if access == 2:
    user_withdraw_amt = float(input("Please Enter your withdraw amount: "))
    if user_withdraw_amt > user_balance:
        print(f"Your withdraw amount is greater than your current balance. Please enter a valid amount.")
    else:
        total_balance_new = user_balance - user_withdraw_amt
        print(f"Your total balance after withdraw is {total_balance_new}.")

if access == 3:
    print(f"Thankyou {user_name} for using our atm! have a great day!")

print(user_access(user_balance, user_depo_balance, user_withdraw_amt))