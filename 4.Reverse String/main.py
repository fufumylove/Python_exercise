# Take a string from user and reverse it

# a example here:
original_string = "Hello World"
rev_string = original_string[::-1] # string opreations which reverse the string
print(rev_string)

def string_reverse(x):
    reversed_string = x[::-1]
    return reversed_string 

user_input = input("Enter a string: ")
reversed_string = string_reverse(user_input)
print("Reversed String: ",reversed_string)

# 格式b = a[i:j:s],这里的s表示步长(step)，默认为1（-1时即翻转读取）;j默认为(len + 1);a[i:j:1]相当于a[i:j]
# i取负值时，表示倒数第i个
# a[i:j:1] 会忽略第j个数
a = [1,2,3,4,5]
print(a[::-1]) #倒数遍历
print(a[2::-1])
print(a[2::1])
print(a[2::-2]) 
print(a[-2::-1])
print(a[2:4:1])
print(a[1:4:2])
