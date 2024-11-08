# Calculate Binary to Decimal
# Example: 1011 = 1+2+0+8 = 11

# USE:
# 1. Functions
# 2. Tuple Assignment
# 3. User_input

def convert_to_decimal(binary):
    decimal = 0
    reversed_binary = binary[::-1]
    for i in range (len(reversed_binary)):
        two_powered = (2**i) * int(reversed_binary[i])
        decimal = decimal + two_powered
        
    return decimal

user_input = input("Enter the binary here: ")
decimal = convert_to_decimal(user_input)

print(f"the convert of binary {user_input} to decimal is {decimal}")