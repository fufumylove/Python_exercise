# Armstrong number: 153
# How??? Length of 153 = 3
# 1^3 + 5^3 + 3^3 = 153

# Use:
# 1.F-strings

# Addtional tasks:
# 1. Create Function
# 2. Take user input



def is_armstrong_num(number):
    int_number = int(number)
    length_num = len(number)
    arm_strongnumber = sum(int(digit) ** length_num for digit in number ) # ** means ^ and this expression works in strings(number is an example)
    if arm_strongnumber == int_number:
        return True
    else:
        return False
    
user_input = input("Enter a number here: ")

if is_armstrong_num(user_input):
    print(f"{user_input} is an armstrong number")
    
else:
    print(f"{user_input} is not an armstrong number")
    
