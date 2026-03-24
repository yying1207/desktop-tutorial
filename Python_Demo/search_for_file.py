import os
import argparse

# Method 1: Find like utility
# find /etc -iname hosts
for dirname, dirpath, filename in os.walk("/etc"):
    for file in filename:
        if file == "hosts":
            print(os.path.join(dirname, file))


# Method 2: User friendly
# python3 search.py <directory name> <file name> ----- on the command line
my_parser = argparse.ArgumentParser(description="Reading the directory path to find the file")
my_parser.add_argument("pathname",
                       help='Please enter the directory path ')
my_parser.add_argument("filesearch",
                       help=' Please enter the file name to search ')
args = my_parser.parse_args()

for dirname, dirpath, filename in os.walk(args.pathname):
    for file in filename:
        if file == args.filesearch:
            print(os.path.join(dirname, file))


# Find file with specific extension
for dirname, dirpath, filename in os.walk("/etc"):
    for file in filename:
        if file.endswith(".conf"):
            print(os.path.join(dirname, file))
