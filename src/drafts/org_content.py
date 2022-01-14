import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = "https://yanruntao.org/%e4%b8%ad%e8%a5%bf%e6%96%b9%e5%9c%a8%e5%a5%a5%e8%bf%90%e5%88%86%e6%ad%a7%e7%9a%84%e5%ae%9e%e8%b4%a8%e5%88%b0%e5%ba%95%e6%98%af%e4%bb%80%e4%b9%88%ef%bc%9f/"
page = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
fhand = urllib.request.urlopen(page, context=ctx).read().decode('UTF-8')

soup = BeautifulSoup(fhand, 'html.parser')  # soup is a class object
# print(soup.prettify())  # see source code in a prettified format!

print(soup.find('time').get_text())   # soup.find('x') will only find the first 'x'(use .find_all('x') if all)
print(soup.find('h1').get_text(), '\n')

tags = soup('p')    # convert soup to a .ResultSet of lines with tag 'p' (similar with a list, can use .len() method)

for tag in tags:    # read line by line - *tag is .tag type
    if 'class' not in tag.attrs:    # .tag is a special main object in BeautifulSoup
        print(tag.get_text(), '\n')

