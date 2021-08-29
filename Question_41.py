# Write a program which can map() to make a list whose 
# elements are square of elements in [1,2,3,4,5,6,7,8,9,10]

def square_it(num):
    return num**2

a_list = [1,2,3,4,5,6,7,8,9,10]
b_list = list(map(square_it, a_list))

print(b_list)
