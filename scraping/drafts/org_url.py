import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = "https://yanruntao.org/%e5%85%ac%e5%bc%80%e9%a1%b5%e9%9d%a2/all/"
page=urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
fhand = urllib.request.urlopen(page, context=ctx).read().decode('UTF-8')
# print(fhand)
soup = BeautifulSoup(fhand,'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href',None))

# fhand = urllib.request.urlopen('https://yanruntao.org/%e7%ba%aa%e5%bf%b5%e9%98%8e%e5%85%88%e7%94%9f%ef%bc%9a%e4%ba%8c%e4%b8%83%e5%ae%b6%e4%ba%ba%e5%af%84%e8%af%ad/')
# for line in fhand:
#     print(line.decode().strip())

