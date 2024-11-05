# Calculate the factorial of a given number

# USE:
# 1. User_Input
# 2. Functions
# 3. f-string

def factorial_of_number(number):
    factorial = 1
    for i in range(2,number+1):
        factorial = factorial*i
    return factorial

user_input = input('Enter your number here: ')

number = int(user_input)

factorial = factorial_of_number(number)
print(f"{number}'s factorial is {factorial}")