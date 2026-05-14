# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.


def find_numbers():
    found_list = []
    for num in range(2000, 3200):
        if (num % 7 == 0) & (num % 5 != 0):
            found_list.append(str(num))       
    print(",".join(found_list))


#Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a 
# comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, 
# the output should be: 40320

def factorial(num):
    """
    import random
    num = random.randint(1, 10)
    result = 1
    for i in range(num):
        result *= i+1
    print(result)
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)


#Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
# Suppose the following input is supplied to the program: 8 Then, the output should be: 
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
def generate_dict(num):
    dict = {}
    if type(num) is int:
        for i in range(1, num+1):
            dict.update({i : i*i})
    else:
        raise Exception("Please enter integral number !")
        
    return dict


# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list 
# and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 
# Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
def generate_list_and_tuple():
    string = input("Please input numbers separated by comma:")
    r_list = string.split(',')
    r_tuple = tuple(r_list)
    print(r_list, r_tuple)

