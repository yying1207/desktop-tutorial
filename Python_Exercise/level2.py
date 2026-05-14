#Question: Write a program that calculates and prints the value according to the given formula: 
# Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 
# Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 
# The output of the program should be: 18,22,24

def calculation():
    import math
    c = 50
    h = 30
    d = input("Please enter the numbers separated by comma:")
    input_list = d.split(",")
    output_list = []

    for num in input_list:
        q = int(2*c*int(num)/h)
        output_list.append(round(math.sqrt(q)))
                        
    print(",".join(map(str, output_list)))


#Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j. 
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 
# Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

def generate_2d_array():
    row_col_list = [int(x) for x in input("Please enter row and column separated by comma:").split(",")]
    x = row_col_list[0]
    y = row_col_list[1]
    col_list = []
    for i in range(x):
        row_list = []
        for j in range(y):
            value = i*j
            row_list.append(value)
        col_list.append(row_list)
        
    print(col_list)



#Question: Write a program that accepts a comma separated sequence of words as input and prints the words 
# in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied 
# to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

def sort_words():
    in_put = input("Please input words separated by comma:")
    input_list = in_put.split(",")
    print(input_list)
    output = input_list.sort()

    print(" ".join(output))



#Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words 
# after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to 
# the program: hello world and practice makes perfect and hello world again Then, the output should be: 
# again and hello makes perfect practice world

def dedup_and_sort():
    s = input()
    print(" ".join(sorted(list(set(s.split(" "))))))



#Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then 
# check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma 
# separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input 
# by console.

def check_binary():
    binary_string = input("Input 4 digit binary numbers separated by comma:")
    binary_list = binary_string.split(",")

    for x in binary_list:
        d_num = int(x, 2)
        if d_num % 5 == 0:
            print(x)


#Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that 
# each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence 
# on a single line.

def find_even():
    even_list = []
    for num in range(1000,3001):
        if num % 2 != 0:
            even_list.append(num)
    print(",".join(map(str, even_list)))



#Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
# Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: 
# LETTERS 10 DIGITS 3
def find_letters_digits():
    import re
    string = input("Please input string:")
    letter_list = re.findall(r'[a-zA-Z]', string)
    digit_list = re.findall(r'[0-9]', string)

    print(f"LETTERS: {len(letter_list)}")
    print(f"DIGITS: {len(digit_list)}")



#Question: Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 
# Suppose the following input is supplied to the program: Hello world! Then, the output should be: 
# UPPER CASE 1 LOWER CASE 9
def find_upper_lower():
    import re
    string = input("Please input string:")
    lower_letter_list = re.findall(r'[a-z]', string)
    upper_letter_list = re.findall(r'[A-Z]', string)

    print(f"LOWER LETTERS: {len(lower_letter_list)}")
    print(f"UPPER LETTERS: {len(upper_letter_list)}")



#Question: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. 
# Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
def compute():
    a = input("Please input digit value of a:")
    n1 = int( "%s" % a )
    n2 = int( "%s%s" % (a,a) )
    n3 = int( "%s%s%s" % (a,a,a) )
    n4 = int( "%s%s%s%s" % (a,a,a,a) )
    print(n1 + n2 + n3 + n4)



#Question: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated
#  numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, 
# the output should be: 1,3,5,7,9
def find_odd():
    string = input("Please input numbers separated by comma:")
    num_list = string.split(",")
    odd_nums = [x for x in num_list if int(x)%2 != 0]
    print(",".join(map(str, odd_nums)))



#Question: Write a program that computes the net amount of a bank account based a transaction log from console input. 
#The transaction log format is shown as following: D 100 W 200

#D means deposit while W means withdrawal. Suppose the following input is supplied to the program: 
#D 300 D 300 W 200 D 100 Then, the output should be: 500
def test_depoist_withdrawal():
    import re
    string = input("Please input deposit and withdrawal:")
    d_amount = re.findall(r'D\s(\d+)', string)
    w_amount = re.findall(r'W\s(\d+)', string)

    d_num = [int(x) for x in d_amount]
    w_num = [-int(y) for y in w_amount]
    sum = 0
    for x in d_num + w_num:
        sum += x
        
    print(sum)