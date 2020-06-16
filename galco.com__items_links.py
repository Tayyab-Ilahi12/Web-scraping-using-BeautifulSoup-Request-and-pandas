from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
hdr = {'User-Agent': 'chrome/5.0'}
baseUrl = "https://www.galco.com/"
# fetching link of each category
fname = "p"
filename = "categories_links.txt"
f = open(filename,"r+")
link = f.readline()
while link:
    items_link = link.strip()
    if(items_link == "https://www.galco.com/scripts/cgiip.exe/wa/wcat/catalog.htm?familyok=no&cat=ACCE&line=&mfg=&navfamily=HANDTOOL&search-desc=Hand%20Tool"):
        req =  Request(items_link,headers=hdr)
        page = urlopen(req)
        product_fname = "products_link.txt"
        fp = open(product_fname,"a")
        soup = BeautifulSoup(page,"html.parser")
        items_links = []
        for a in soup.find_all('a', href=True):      
            if("?" not in a['href'] and "/buy" in a['href'] and ".exe" not in a['href'] and ".htm" not in a['href']):
                if (a['href'] not in items_links):
                    items_links.append(a['href'])
                    product_link= baseUrl+a['href']
                    fp.write(product_link+"\n")
                else:
                    continue
    elif(items_link == "https://www.galco.com/scripts/cgiip.exe/wa/wcat/catalog.htm?familyok=no&cat=TOOL&line=&mfg=&navfamily=SDRIVERS&search-desc=Driver"):
        for i in range(11):
            i = i + 1
            number = str(i)
            modify_link = "https://www.galco.com/scripts/cgiip.exe/wa/wcat/catalog.htm?cat=TOOL&familyok=no&searchbox=Driver&mfg=&line=&itemsperpage=20&pagenum="+number+"&pgend=11&div=CP&navfamily=SDRIVERS&sortbyoption=pop"
            print(modify_link)
            req =  Request(modify_link,headers=hdr)
            page = urlopen(req)
            product_fname = "products_link.txt"
            fp = open(product_fname,"w")
            soup = BeautifulSoup(page,"html.parser")
            items_links = []
            for a in soup.find_all('a', href=True):      
                if("?" not in a['href'] and "/buy" in a['href'] and ".exe" not in a['href'] and ".htm" not in a['href']):
                    if (a['href'] not in items_links):
                        items_links.append(a['href'])
                        product_link= baseUrl+a['href']
                        fp.write(product_link+"\n")
                    else:
                        continue
    else:
        for i in range(3):
            i = i+1
            s = str(i)
            url =  items_link+"?pagenum="+s
            print(url)
            req =  Request(url,headers=hdr)
            page = urlopen(req)
            product_fname = "products_link.txt"
            fp = open(product_fname,"w")
            soup = BeautifulSoup(page,"html.parser")
            items_links = []
            for a in soup.find_all('a', href=True):      
                if("?" not in a['href'] and "/buy" in a['href'] and ".exe" not in a['href'] and ".htm" not in a['href']):
                    if (a['href'] not in items_links):
                        items_links.append(a['href'])
                        product_link= baseUrl+a['href']
                        fp.write(product_link+"\n")
                else:
                    continue
    link = f.readline()
