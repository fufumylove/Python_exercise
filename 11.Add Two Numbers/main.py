# Take two number inputs from user, print the sum

# USE:
# 1. User_Input
# 2. Functions
# 3. f-string

def add_nums(num1, num2):
    sum = num1 + num2
    return sum

first_num = input('Enter first number here:')
second_num = input('Enter second number here:')

first_num = int(first_num)
second_num = int(second_num)

sum = add_nums(first_num, second_num)

print(f"Sum of {first_num} and {second_num} is {sum}")