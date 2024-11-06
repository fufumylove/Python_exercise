# Calculate LCM
# Example: LCM of 6, 8 is 24
# Formula: a*b = DCG(a,b)*LCM(a,b)


# USE:
# 1.Functions
# 2.F-strings

# Additional task:
# 1.Calculate the LCM of User Input

import math

def calc_lcm(a,b):
    """_summary_

    Args:
        a (integer)
        b (integer)

    Returns:
        integer: The lcm of a and b
    """    
    gcd = math.gcd(a,b)
    lcm = (a*b)//gcd
    return lcm

user_input_num1 = input("Enter first number here: ")
user_input_num2 = input("Enter second number here: ")

int_user_input_num1 = int(user_input_num1)
int_user_input_num2 = int(user_input_num2)

lcm = calc_lcm(int_user_input_num1, int_user_input_num2) # use myfunction 
LCM = math.lcm(int_user_input_num1, int_user_input_num2)


print(f"The LCM of {user_input_num1} and {user_input_num2} is {lcm}")

if(lcm == LCM):
    print("The answer is True !")