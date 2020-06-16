from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#starting site request

product_fname = "products_link.txt"
fp = open(product_fname,"w")
base_url = "https://www.predig.com"

for page_index in range(72):
    
    site= "https://www.predig.com/quickshop?combine=PD&page="+str(page_index)
    hdr = {'User-Agent': 'chrome/5.0'}
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,"html.parser")
    
    s = soup.findAll('td',{'class':"views-field views-field-views-conditional-6"})
    for i in s:
        p = i.find('a',href = True)
        d = p['href']
        item_url = base_url+d
        fp.write(item_url+"\n")
           
    print(site + " All links extracted")

fp.close()
