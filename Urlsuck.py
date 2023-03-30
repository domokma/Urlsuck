import requests
import re
import time
import os

# 填写url
url = input("输入要吸的url：")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
requests.packages.urllib3.disable_warnings()
response = requests.get(url, headers=headers, verify=False)
pattern = re.compile('(https?://[^\s]+)')
urls = pattern.findall(response.text)
print("list1：", urls)
urls2 = []
for url in urls:
    try:
        response = requests.get(url, headers=headers, verify=False)
        urls2 += pattern.findall(response.text)
    except:
        pass
print("list2：", urls2)
filename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".txt"
with open(filename, "w") as f:
    f.write("list1：\n")
    for url in urls:
        f.write(url + "\n")
    f.write("\nlist2：\n")
    for url in urls2:
        f.write(url + "\n")
print("suck complete：", filename)

os.startfile(filename)
