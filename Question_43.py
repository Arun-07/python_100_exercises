# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# a_list = [i for i in range(1, 21) if i % 2 == 0]
# print(a_list)

def filter_even(num):
    return num % 2 == 0

a_list = list(filter(filter_even, range(1, 21)))
print(a_list)
