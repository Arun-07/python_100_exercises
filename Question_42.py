# Write a program which can map() and filter() to make a list 
# whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

def square_it(num):
    return num**2

def filter_even(num):
    return num if num % 2 == 0 else 0

a_list = [1,2,3,4,5,6,7,8,9,10]
b_list = list(map(square_it, a_list))
c_list = list(filter(filter_even, b_list))

print('Squared list is: ', b_list)
print('Filtered even list is: ', c_list)