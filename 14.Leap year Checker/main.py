# Take User input of the year: Example 2024
# Print 2024 is a /is not a leap year

# Criterial
# 1. should be divisible by 4, but not by 100
# 2. Or should be divisible by 400

# Use:
# 1. User Input
# 2. Functions
# 3. f-strings

def is_leap_year(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        return True
    else:
        return False
    
user_year = input("Enter year here: ")
if is_leap_year(int(user_year)):
    print(f"{user_year} is a leap year")
    
else:
    print(f"{user_year} is not a leap year")