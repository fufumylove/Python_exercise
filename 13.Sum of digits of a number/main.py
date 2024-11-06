# Input = 12345
# Output = 1+2+3+4+5 = 15

# Use:
# 1.List comprehension
# 2.F-strings


# Addtional task: Take input from user

number = 23456
str_number = str(number)

sum_nums = sum(int(digit) for digit in str_number)
print(f"The sum of {number} is {sum_nums}")


# Addtional task solution :

user_input = input("Enter a number here :")

sum_numbers = sum(int(digits) for digits in user_input)
print(f"The sum of {user_input} is {sum_numbers}")