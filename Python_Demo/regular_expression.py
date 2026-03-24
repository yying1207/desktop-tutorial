import re

with open('access_log') as f:
    fread = f.read()

    regex = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" # 匹配IP地址的正则表达式
    iplist = re.findall(regex, )
    print(iplist)