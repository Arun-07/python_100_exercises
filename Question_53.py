# Assuming that we have some email addresses in the "username@companyname.com" format, 
# please write program to print the user name of a given email address. 
# Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program: john@google.com
# Then, the output of the program should be: john

## my solution ##
# def get_username(email):
#     letter_list = []
#     for letter in email:
#         if letter == '@':
#             break
#         letter_list.append(letter)
#     return ''.join(letter_list)

# print(get_username("john@google.com"))


import re

email = "john@google.com"
pattern = "(\w+)@\w+.com"
name = re.findall(pattern,email)
print(name)