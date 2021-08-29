# Define a function that can convert a integer into a string and print it in console.

def int_to_string(int_list):
    for i in int_list:
        print(str(i), end=' ')
    return 0

int_list = [1, 2, 3, 4, 5]
int_to_string(int_list)
