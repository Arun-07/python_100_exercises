# Define a function which can print a dictionary where the keys are 
# numbers between 1 and 20 (both included) and the values are square of keys.

def squared_dict():
    return {i:i**2 for i in range(1, 21)}

print(squared_dict())
