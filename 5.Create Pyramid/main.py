# Draw Pyramid using *
#    *
#   ***
#  *****
# *******
#********* 
# 5 x 5 Pyramid above

rows = 10

for i in range(1, rows + 1):
    # Print spaces
    print(" " *(rows-i), end="") # hints: end=\n (default), e.g. end='\t',means 制表符
    
    # Print *
    print("*" *(2*i - 1))
    

