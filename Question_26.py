# Define a function which can compute the sum of two numbers.

def add_func(a, b):
    return a + b

a, b = list(map(int, input("Enter two numbers sperated by coma: ").split(',')))
print(add_func(a, b))
