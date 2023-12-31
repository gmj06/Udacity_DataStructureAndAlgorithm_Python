"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions.
Fibonacci Sequence: 1,1,2,3,5,8,13,21,34,55,89,144,.."""

def get_fib(position):
    if position == 0 or position == 1:
        return position
        
    output = get_fib(position - 1) + get_fib(position - 2)
    return output

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
