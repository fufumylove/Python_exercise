# Calculate GCD, use Euclidean algorithm


# Use:
# 1.Function
# 2.Tuple Assignment


"""
--------------------------------------
# 从元组中分配多个值到单独的变量
person = ("Alice", 30, "工程师")

name, age, profession = person

print(name)       # 输出: Alice
print(age)        # 输出: 30
print(profession) # 输出: 工程师
--------------------------------------
#元组赋值常用于不使用临时变量来交换两个变量的值：
x, y = 5, 10
x, y = y, x

print(x)  # 输出: 10
print(y)  # 输出: 5
-------------------------------------
#可以使用 * 操作符来捕获剩余的元素
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers

print(first)    # 输出: 1
print(middle)   # 输出: [2, 3, 4]
print(last)     # 输出: 5

"""





a = 12
b = 36

def calc_gcd(num1, num2):

    while(num2):
        print("Starting")
        print(num1)
        print(num2)
        num1, num2 = num2, num1%num2 # Tuple Assignment: 元组赋值,可以一次性将多个值从一个元组分配给多个变量
        print("After %")
        print(num1)
        print(num2)
    return num1

gcd = calc_gcd(a, b)
print(f"The GCD of {a} and {b} is {gcd}")