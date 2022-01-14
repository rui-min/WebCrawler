import urllib.request,urllib.parse,urllib.error
import pandas as pd
import ssl

# avoid cert issue
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE

# create dataframe
ex_file = r'C:\Users\MINRUI\Desktop\RTY collection.xlsx'
sheet = 0
df = pd.read_excel(io=ex_file, sheet_name=sheet)

# iterate by itertuples method
for row in df.itertuples():
    url = row[1]
    print(url)
    # page = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # fhand = urllib.request.urlopen(page, context=ctx).read().decode('UTF-8')
    # con = pd.read(fhand)
    # fhand.read()
    # content.to_excel(io=file_name, sheet_name=r[0])


#change NameOfTheSheet with the sheet name that includes the data
# data = pd.read_excel(path1, sheet_name="NameOfTheSheet")

#save it to the 'NewSheet' in destfile
# data.to_excel(path2, sheet_name='NewSheet')