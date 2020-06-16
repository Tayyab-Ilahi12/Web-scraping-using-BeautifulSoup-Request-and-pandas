from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd

results = []
#starting site request

site= "https://www.predig.com/products/product_series/consolidator-plus"
hdr = {'User-Agent': 'chrome/5.0'}

#requesting connection to the page
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page,"html.parser")
product = soup.findAll('article')

###Why buy box
for i in product:
    
    ## Title
    t = i.find('div','field-items')
    print("Title: " + t.text)
    
    ## Description
    d = i.find('p')
    if(d is not None):
        descp = d.text
   
    ##  Why buy box
    why = []
    find_why_buy = i.find("div",'why_buy_box')
    if(find_why_buy is not None):
        why_buy_box = find_why_buy.findAll('li')
        for j in why_buy_box:
            why.append(j.text)
    else:
        why.append("Not feauture available")
    
    results.append((t.text,descp,repr(why)))
    
df = pd.DataFrame(results, columns = ['Title','Description','Feature'])
df.to_csv('products.csv', mode = 'a', index = False,encoding='utf-8',header=False)
print("done")