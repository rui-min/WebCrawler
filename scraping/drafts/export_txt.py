import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl

# to avoid no cert error
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

url = "https://blog.wenxuecity.com/myblog/1666/202010/25516.html"
page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
fhand = urllib.request.urlopen(page, context=ctx).read().decode('UTF-8')

with open("output.txt", "a") as f:

    soup = BeautifulSoup(fhand, 'html.parser')  # soup is a class object

    print(soup.find('h2').get_text(), file=f)   # soup.find('x') will only find the first 'x'(use .find_all('x') if all)

    tags = soup('span')    # convert soup to a .ResultSet of lines with tag 'span' (similar with a list, can use .len() method)
    for tag in tags:    # read line by line - tag is .tag type
        if 'class' in tag.attrs and tag['class'][0] == 'time':    #! <span class="time BLK_txtc"> has ['time', 'BLK_txtc'] as class value!
            print(tag.get_text(), '\n', file=f)
            break

    tags = soup('p')    # convert soup to a .ResultSet of lines with tag 'p' (similar with a list, can use .len() method)
    for tag in tags:    # read line by line - *tag is .tag type
        if 'class' not in tag.attrs:    # .tag is a special main object in BeautifulSoup
            print(tag.get_text(), '\n', file=f)

    print("======================================================", '\n', file=f)


    tags = soup('div', attrs={'class': 'comment-r'})    # convert soup to a .ResultSet of lines with tag 'div' and class = 'comment-r'

    for tag in tags:
        if tag.contents[1].contents[1].contents == ['润涛阎']:
            print('润涛阎 comment:', file=f)
            for line in tag.contents[9].contents:
                try:
                    print(line.strip(), file=f)
                except:
                    continue
            print('------------------------------------------------------------------', file=f)