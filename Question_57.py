# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

user_input = input()
unicoded = user_input.encode("utf-8")

print(unicoded)
