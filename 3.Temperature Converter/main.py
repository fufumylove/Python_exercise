# convert Celsius to Fahrenheit

def celsius_to_fahrenheit(x):
    fahrenheit = (x *9/5) + 32
    return fahrenheit
    


user_input = input("Enter Celsius Degrees: ") # tips: 用户输入默认为string!
number = int(user_input)

converted_celsius = celsius_to_fahrenheit(number)
print("Converted Temp", converted_celsius)