# A String is a palindrome is the reverse of the string is same as the original string
# Example: racecar == racecar(reverse)

# USE:
# 1. User_input
# 2. Functions
# 3. f-string


def is_palindrome(astring):
 astring = astring.lower()
 reversed_st = astring[::-1]
 if astring == reversed_st:
    return True
 else:
    return False 

user_input = input('Enter your string here: ')

if(is_palindrome(user_input)):
   print(f"{user_input} is a palindrome!")
else:
   print(f"{user_input} is not a palindrome!")

