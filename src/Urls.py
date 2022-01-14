import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

"""
python ignore certificate validation urllib2
https://stackoverflow.com/questions/19268548/python-ignore-certificate-validation-urllib2
"""
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def indexDictGenerator():
    """
    There are 16 pages in total, "...page=" + i + "..." is the generic format of index pages (i=0~15)
    :return: the dictionary "indexDict" with {title+date, url link} pairs
    """
    indexDict = {}

    for i in range(16):
        url = "https://blog.wenxuecity.com/blog/frontend.php?page=" + str(i) + "&act=articleList&blogId=1666"
        # print(url)

        page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        fhand = urllib.request.urlopen(page, context=ctx).read().decode('UTF-8')

        soup = BeautifulSoup(fhand, 'html.parser')  # soup is a class object
        # print(soup.prettify())  # see source code in a prettified format!

        tags = soup('div', attrs={'class': 'articleCell BLK_j_linedot1'})


        for tag in tags:
            # print(tag)    # investigate the structure of one tag
            url2 = tag.a.get('href')
            title = tag.a.get_text().strip()
            # note class is a reserved word and class_ is used; .find_all() will return a list-like result
            date = tag.find_all('span', class_="atc_tm BLK_txtc")[0].get_text() # use .find ok here but [0] removed
            date = date.strip()[0:10]   # only date needed
            content = title+date
            indexDict[content] = f"https://blog.wenxuecity.com{url2}"

    return indexDict


if __name__ == "__main__":
    print(indexDict())  # for testing only
