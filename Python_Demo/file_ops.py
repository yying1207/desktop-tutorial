import os

# create a file
with open("tempfile", "w") as f:
    f.writelines(["Line 1\n", "Line 2\n", "Line 3\n"])
    print("file path: ", os.path.abspath("tempfile"))

# read a file
with open("tempfile", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')