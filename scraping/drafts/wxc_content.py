import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# to avoid no cert error
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

# use 'Mozilla/5.0' to pretend to be a web explorer and get around the security check
url = "https://blog.wenxuecity.com/myblog/1666/202010/25516.html"
page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
fhand = urllib.request.urlopen(page, context=ctx).read().decode('UTF-8')

# build a soup (initialise the class)
soup = BeautifulSoup(fhand, 'html.parser')  # soup is a class object
# print(soup.prettify())  # see source code in a prettified format!

# the first 'h2' is the title (by inspecting the original webpage)
print(soup.find('h2').get_text())   # soup.find('x') will only find the first 'x'(use .find_all('x') if all)

# find the date of editing (by inspecting the original webpage)
tags = soup('span')    # convert soup to a .ResultSet of lines with tag 'span' (similar with a list, can use .len() method)
for tag in tags:    # read line by line - tag is .tag type
    if 'class' in tag.attrs and tag['class'][0] == 'time':    #! <span class="time BLK_txtc"> has ['time', 'BLK_txtc'] as class value!
        print(tag.get_text(), '\n')
        break

# find the body content by souping 'p' tags
tags = soup('p')    # convert soup to a .ResultSet of lines with tag 'p' (similar with a list, can use .len() method)
for tag in tags:    # read line by line - *tag is .tag type
    if 'class' not in tag.attrs:    # .tag is a special main object in BeautifulSoup
        print(tag.get_text(), '\n')

print("======================================================", '\n')


# find comments (by inspecting the original webpage)
tags = soup('div', attrs={'class': 'comment-r'})    # convert soup to a .ResultSet of lines with tag 'div' and class = 'comment-r'

#! Deal with following kinds of 'div' sub-contents

# ['\n', <span class="comment_username">
# <a href="/myblog/75839/" target="_blank">阿乐泰</a>
# </span>, '\n', <span class="comment_dateline">
# <em class="BLK_txtc">2020-10-29 13:30:50</em>
# </span>, '\n', <span class="comment_reply" username="阿乐泰">
# <a href="#addComment">回复</a>
# </span>, '\n', <span class="comment_reply">
# <a href="//www.wenxuecity.com/qqh/index.php?act=write&amp;cid=%E9%98%BF%E4%B9%90%E6%B3%B0">悄悄话</a>
# </span>, '\n', <span class="comment_msgbody">
# <br/>富兰克林又喜欢钱又喜欢女人，所以就不竞选总统啦，因为懂得老阎的第n条定律呗。
#                 </span>, '\n']
for tag in tags:
    if tag.contents[1].contents[1].contents == ['润涛阎']:
        print('润涛阎 comment:')
        for line in tag.contents[9].contents:
            try:
                print(line.strip())
            except:
                continue
        print('------------------------------------------------------------------')