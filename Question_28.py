# Define a function that can receive two integer numbers in string form 
# and compute their sum and then print it in console.

def sum_func(a, b):
    return int(a) + int(b)

a, b = input("Enter two numbers: ").split(',')
print(sum_func(a, b))
