# You are required to write a program to sort the (name, age, score) tuples 
# by ascending order where name is string, age and score are numbers. 
# The tuples are input by console. The sort criteria is:
'''
1: Sort based on name
2: Then sort based on age
3: Then sort by score
'''
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
'''
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
'''
# Then, the output of the program should be: 
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

student_list = []
while True:
    student_info = tuple(input().split(','))
    if not student_info[0]:
        break
    else:
        student_list.append(student_info)

student_list.sort(key=lambda k:(k[0], int(k[1]), int(k[2])))
print(student_list)