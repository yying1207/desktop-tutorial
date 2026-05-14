import re

#Question: A website requires the users to input username and password to register. Write a program to check the validity 
# of password input by users. Following are the criteria for checking the password:

#At least 1 letter between [a-z]
#At least 1 number between [0-9]
#At least 1 letter between [A-Z]
#At least 1 character from [$#@]
#Minimum length of transaction password: 6
#Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and 
# will check them according to the above criteria. Passwords that match the criteria are to be printed, 
# each separated by a comma. Example If the following passwords are given as input to the program: 
# ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1

def validate_pwd():
    passwords = input("Please input password:")
    pwd_list = passwords.split(",")
    validate_list = []

    for pwd in pwd_list:
        if 6 <= len(pwd) <= 12 and re.search(r"[a-z]", pwd) and re.search(r"[A-Z]", pwd) and re.search(r"[0-9]", pwd) and re.search(r"[$#@]", pwd):
            validate_list.append(pwd)
            
    print(",".join(validate_list))


#Question: You are required to write a program to sort the (name, age, height) tuples by ascending order where name is 
# string, age and height are numbers. The tuples are input by console. The sort criteria is: 
# 1: Sort based on name; 
# 2: Then sort based on age; 
# 3: Then sort by score. The priority is that name > age > score. 
# If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, 
# the output of the program should be: 
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
import re

def sort_stu_info():
    stu_info = input("Please input student info:")
    stu_list = re.split(r"[,\s]+", stu_info)
    stu_tuple_list = []
    for i in range(0, len(stu_list), 3):
        stu_tuple_list.append((stu_list[i], stu_list[i+1], stu_list[i+2]))

    print(sorted(stu_tuple_list, key=lambda x: (x[0], x[1], x[2])))



#Question: Define a class with a generator which can iterate the numbers, which are divisible by 7, 
# between a given range 0 and n.

def test_divide_seven(n):
    for i in range(1, n+1):
        if i % 7 == 0:
            yield i
        
n = int(input("Please input n:"))
for i in test_divide_seven(n):
    print(i)


