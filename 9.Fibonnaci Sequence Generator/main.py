# Generate Fibonnaci sequence upto user provided input
# Example: n = 5, fib sequence = 0, 1, 1, 2, 3

# USE:
# 1. User_Input
# 2. Functions
# 3. f-string

def gen_fib(n):
    fibo_seq = [0,1]
    
    while len(fibo_seq) < n:
        next_term = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_term)
        
    return fibo_seq

user_input = input("Enter the length of Fibonnaci Sequence: ")
num_input = int(user_input)

seq = gen_fib(num_input)

print(f"The first {num_input} terms of the Fibonnaci Sequence is {seq}")
