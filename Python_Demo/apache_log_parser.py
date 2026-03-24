import re
import csv
import argparse
from collections import Counter
# Step 1: Open the log file
# Step 2: Extracting IP addresses from the log file
# Step 3: Counting the occurrences of each IP address
# Step 4: Save the output of the program in the csv file
# Step 5: Make program user-friendly:
#  - User has the option to provide its own log file
#  - Add the help option: -h
#  - 


logfile = "apache_log"
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
"""
with open(logfile) as f:
    log = f.read()
    ip_list = re.findall(pattern, log)
    ip_count = Counter(ip_list)
    for ip, count in ip_count.items():
        print(f"{ip}: {count}")

    with open("ipcount.csv", "w") as f:
        fwritecsv = csv.writer(f)
        fwritecsv.writerow(["IP Address", "Count"])
        for ip, count in ip_count.items():
            fwritecsv.writerow([ip, count])
"""

my_parser = argparse.ArgumentParser(description="Reading the log file")
my_parser.add_argument("logfile",
                       help="Please enter the log file to parse",
                       type=argparse.FileType('r'))
args = my_parser.parse_args()

with args.logfile as f:
    log = f.read()
    ip_list = re.findall(pattern, log)
    ip_count = Counter(ip_list)
    for ip, count in ip_count.items():
        print(f"{ip}: {count}")

    with open("ipcount.csv", "w") as f:
        fwritecsv = csv.writer(f)
        fwritecsv.writerow(["IP Address", "Count"])
        for ip, count in ip_count.items():
            fwritecsv.writerow([ip, count])
