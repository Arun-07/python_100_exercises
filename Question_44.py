# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

def square_it(num):
    return num**2

sqrd_list = list(map(square_it, range(1, 21)))

print(sqrd_list)

# sqrd_list = list(map(lambda x: x**2, range(1, 21)))
# print(sqrd_list)
