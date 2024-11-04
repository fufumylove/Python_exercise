# Check if a user input is a prime
# Prime number is only divisible by 1 and itself

# USE
# 1. User Input
# 2. Functions
# 3. f-strings

def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2,int(number)+1):
        if number%i==0:
         return False
    return True

user_input = input("Enter the number here: ")
number = int(user_input)
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
# Additional Tasks ->Optimize the program


