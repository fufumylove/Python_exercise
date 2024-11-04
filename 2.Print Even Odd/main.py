# take user input and print if the number is even or odd

user_input = input("Enter number here: ")
number = int(user_input)

if(number % 2 == 0):
    print(number, "is even")
else:
    print(number, "is odd")