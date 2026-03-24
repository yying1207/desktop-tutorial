import os
import sys

if not os.path.exists("/etc/xx"):
    sys.exit() # exit the program with a non-zero exit code, indicating an error condition. You can also provide an optional argument to sys.exit() to specify the exit code or message. For example, sys.exit(1) would exit with a status code of 1, which is commonly used to indicate a general error.

if len(sys.argv) != 3:
    print("This script needs at least 3 command line arguments. ")
    sys.exit()

print("All command line arguments:", sys.argv)
print("First command line argument:", sys.argv[0]) # the name of the script being executed
print("Second command line argument:", sys.argv[1]) # the first argument passed to the script
print("Third command line argument:", sys.argv[2]) # the second argument passed to the script
