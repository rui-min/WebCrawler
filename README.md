# Web Crawler Documentation
* This is a simple web crawler grabbing a Chinese author's 916 blogs' contents and comments to 916+1 .docx files (there is 1 index file).
* list of articles link(page 1): https://blog.wenxuecity.com/blog/frontend.php?page=0&act=articleList&blogId=1666

# Copyright
**Copyright 100% belongs to original author Mr. Runtao Yan (润涛阎) and the blog platform, not for any kind of business usage.**
**©版权100%永久归作者及文学城平台所有，转载须知**

# Quick Start
Run export_wxc.py

# Functionality of each file


# Libraries (installed or put under same project folder)
1. Major External library: Beautiful Soup 4("bs4"); For details please refer to https://github.com/wention/BeautifulSoup4
2. Others: 
     1. docx; For details please refer to https://github.com/python-openxml/python-docx
     2. lxml;
     3. urllib; 
     4. ssl; 
     
# Limitations
1. No protection for internet interruption: everything needs to be done in a consecutive period of time without interruption(which can vary from 10 to 50 minutes depending on internet condition).
2. There are less than 5 articles which can not be grabbed normally. It is due to library docx's incompatiblity with some non-English characters. The few articles(<5) are skipped by try... except.. clause.

# References
1. Beautiful Soup 4 Documentation
*https://www.crummy.com/software/BeautifulSoup/bs4/doc/*
2. python-docx Documentation
*https://python-docx.readthedocs.io/en/latest/*
3. python ignore certificate validation urllib2
https://stackoverflow.com/questions/19268548/python-ignore-certificate-validation-urllib2
4. Set paragraph font in python-docx
*https://stackoverflow.com/questions/27884703/set-paragraph-font-in-python-docx*
5. python-docx operate word file (Chinese font setting!)
*https://codestudyblog.com/cnb/0625084821.html*
6. UserAgentString.com - List of Chrome User Agent Strings (web scraping)
*http://www.useragentstring.com/pages/useragentstring.php?name=Chrome*
7. Direct print output to a .txt file
*https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file*
