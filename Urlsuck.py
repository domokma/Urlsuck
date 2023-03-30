import requests
import re
import time
import os

# 填写url
url = input("请输入地址：")
# 访问时带上user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
# 通过requests关掉警告
requests.packages.urllib3.disable_warnings()
# 访问url
response = requests.get(url, headers=headers, verify=False)
# 通过正则表达试提取页面中包括http和https的url地址和跳转地址，生成列表1
pattern = re.compile('(https?://[^\s]+)')
urls = pattern.findall(response.text)
print("列表1：", urls)
# 再次访问列表1中的url，再次重复提取页面的url，生成列表2
urls2 = []
for url in urls:
    try:
        response = requests.get(url, headers=headers, verify=False)
        urls2 += pattern.findall(response.text)
    except:
        pass
print("列表2：", urls2)
# 将列表1，列表2的结果print出来，并且输出到txt，文件名使用当前系统时间命名
filename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".txt"
with open(filename, "w") as f:
    f.write("列表1：\n")
    for url in urls:
        f.write(url + "\n")
    f.write("\n列表2：\n")
    for url in urls2:
        f.write(url + "\n")
print("结果已输出到文件：", filename)

os.startfile(filename)
