# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.

import re

odd_pattern = re.compile(r"['1', '3', '5', '7', '9' ]")

for num in range(1000, 3000):
    if num%2 == 0:
        if not odd_pattern.search(str(num)):
            print(num, end=' ')




