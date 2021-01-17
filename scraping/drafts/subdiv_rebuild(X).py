import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# to avoid no cert error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# use 'Mozilla/5.0' to pretend to be a web explorer and get around the security check
url = "https://blog.wenxuecity.com/myblog/1666/202010/25516.html"
page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
fhand = urllib.request.urlopen(page, context=ctx).read().decode('UTF-8')

#! main part - create a sub-soup
soup = BeautifulSoup(fhand, 'html.parser')
tags = soup('div', attrs={'class': 'comment-r'})    # convert soup to a .ResultSet of lines with tag 'div' and class = 'comment-r'
new = ''
for tag in tags:
    new += str(tag)
com_soup = BeautifulSoup(new,'html.parser')
print(com_soup)
