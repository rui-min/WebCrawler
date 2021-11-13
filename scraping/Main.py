'''
IMPORTANT: 0. Please do NOT repeatedly run this program in a short period of time
1. Use a stable VPN if in mainland China
2. Ensure library folders for BeautifulSoup4 renamed to "bs4", python-docx renamed to "docx"; install lxml
3. No protection for internet interruption: everything needs to be done in a consecutive period of time
    without interruption(which is usually 10-40 minutes).
'''

import datetime
import Urls, Index, Files

if __name__ == "__main__":
    print(datetime.datetime.now())  # start run-time

    """
    prompt to input the directory part of the full path
    full path example: C:\\Users\\<username>\\Desktop\\index.docx
    """
    pathPrefix = input("Please input an existing directory for 917 files storage(e.g.C:\\Users): ")

    """
    next 3 lines: for details, please check Urls.py, Index.py, and Files.py
    """
    indexDict = Urls.indexDictGenerator()        # assign the dictionary "indexDict" with {title+date, url link} pairs
    Index.titleGenerator(indexDict, pathPrefix+f"\\index.docx")     # generate index.docx file
    Files.filesGenerator(indexDict, pathPrefix)         # generate 916 docx files for 916 articles


    print(datetime.datetime.now())  # End run-time
