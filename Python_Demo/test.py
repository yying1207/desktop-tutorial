# os module usage
import os
if os.path.exists("/etc/abc1234"):
    sys.exit()



# getuser usage
import getpass, sys
print(f"Current user: {getpass.getuser()}")
sys.exit()


# getpass usage
import getpass, sys
password = input("Please enter your password: ") # old way, not secure
password = getpass.getpass("Please enter your secure password: ") # new way, secure, the input will be hidden
print(f"Your password is: {password}")
sys.exit()



# sys.argv usage
import sys
print(f"argvs: {sys.argv}")
print(f"script name: {sys.argv[0]}") # The name of the script being executed
print(f" argv 1: {sys.argv[1]}") # The first argument passed to the script (after the script name)
print(f" argv 2: {sys.argv[2]}")


if len(sys.argv) != 1:
    sys.exit()





