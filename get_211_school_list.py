# 获取211学校名单
import re

from bs4 import BeautifulSoup
import requests

url = "https://daxue.eol.cn/985.shtml"
response = requests.get(url)
response.encoding = 'utf8'
html = response.text
# print(html)
# soup =BeautifulSoup(html, 'html.parser')
# print(soup.select("tbody"))
mo = r'>[\u4e00-\u9fa5]+?大学<'
# mo = r'[\u4e00-\u9fa5]+?大学[（\u4e00-\u9fa5）]+?<'
pa = re.compile(mo)
res = pa.findall(html)
print(res)
fout = open("b.txt", 'w+', encoding="utf8")
for a in res:
    # if '正规' in a or '双一流' in a:
    #     continue
    t = a[1:-1]
    fout.write(t)
    fout.write("\n")

fout.close()
