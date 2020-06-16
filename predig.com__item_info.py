from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd
#starting site requests

results = []

def item_info(str):
    ######### starting site request
    site= str
    hdr = {'User-Agent': 'chrome/5.0'}
    #requesting connection to the page
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,"html.parser")
    content = soup.find("div","tab-content product-overview--tab-panels")    
    c = content.findAll('span')
    #title
    title = c[2].text
    #product type
    product_type = c[5].text
    
    df = pd.DataFrame(results, columns = ['Title','Description'])
  
    results.append((title,product_type))
    
    print("DONE")



fp = open("products_link.txt","r")
link = fp.readline()
while link:
    item_info(link)
    link = fp.readline()



