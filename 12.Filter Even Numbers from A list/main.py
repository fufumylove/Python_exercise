# Suppose the given list is [1,2,3,4,5,6,7,8,9]
# The output shoule be [2,4,6,8]

# Use:
# 1. List Comprehension
# 2. F-strings


numbers = [10,11,12,13,14,15,16,17,18,19]
Filtered_list = []
for num in numbers:
     if num%2 == 0:
       Filtered_list.append(num)

print(f"The filtered list is {Filtered_list}")
    
    
# another effient method:
Filtered_list_fast = [num for num in numbers if num%2 == 0]
print(f"The filtered list is {Filtered_list_fast}")