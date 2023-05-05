import tkinter as tk
import requests
import re
import time
import os

def get_urls():
    url = entry.get()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url, headers=headers, verify=False)
    pattern = re.compile('(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)')
    urls = pattern.findall(response.text)
    urls2 = []
    for url in urls:
        try:
            response = requests.get(url, headers=headers, verify=False)
            urls2 += pattern.findall(response.text)
        except:
            pass
    filename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".txt"
    with open(filename, "w") as f:
        f.write("列表1：\n")
        for url in urls:
            f.write(url + "\n")
        f.write("\n列表2：\n")
        for url in urls2:
            f.write(url + "\n")
    os.startfile(filename)
root = tk.Tk()
root.title('Urlsuck by:domokma')
label = tk.Label(root, text='输入RUL（需要带上http协议）:')
label.pack()
entry = tk.Entry(root, width=50)
entry.pack()
button = tk.Button(root, text='suck!!!', command=get_urls)
button.pack()
root.mainloop()
