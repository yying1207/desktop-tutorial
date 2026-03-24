import os
import pathlib

open("abc.txt") #FileNotFoundError: [Errno 2] No such file or directory: 'abc.txt'

os.system("touch filetest")
os.system("ls -l filetest")
os.system("chmod 100 filetest")
open("filetest") #PermissionError: [Errno 13] Permission denied: 'filetest'


open(".etc") # IsADirectoryError: [Errno 21] Is a directory: '.etc'



# Method 1: Catch the exception and print the error message
try:
    open("/etc/hosts")
except Exception as e:
    print(e)

# Method 2: Check file or directory exists
if os.path.exists("/etc/hosts"):
    open("/etc/hosts")
else:    
    print("The file or directory does not exist.")


print(os.path.isfile("abc.txt")) # True
print(os.path.isdir("abc.txt")) # False
print(os.path.isfile("/etc")) # False
print(os.path.isdir("/etc")) # True


filename = "/etc/hosts"
if os.path.exists(filename) and os.path.isfile(filename):
    open(filename)
else:
    print(f"{filename} does not exist or is not a file.")





# pathlib
path = pathlib.Path("/etc/hosts")
if path.exists() and path.is_file():
    open(path)
else:    print(f"{path} does not exist or is not a file.")
            