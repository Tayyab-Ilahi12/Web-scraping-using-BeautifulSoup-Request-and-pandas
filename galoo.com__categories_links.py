from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

#starting site request
site= "https://www.galco.com/get/Hand-Tools"
hdr = {'User-Agent': 'chrome/5.0'}

#requesting connection to the page
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page,"html.parser")
page.close()

#merging links for further scrapinng
base_url1 = "https://www.galco.com"
url_list_cat = []

#Creating a csv file
filename = "categories_links.txt"
f = open(filename,"w")

#scraping links of categories and saving into a list named:url_list_cat
def get_url(str):
        #requesting connection to the page
    req = Request(str,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,"html.parser")
    for a in soup.find_all('a', href=True):
        if("?" in a['href'] or "galco" in a['href'] or "with-confidence" in a['href']):
            continue
        else:
            if ("/shop" in a['href'] or "/get" in a['href']):
                temp = base_url1 + a['href']
                # cat = categories
                if temp not in url_list_cat:
                    url_list_cat.append(temp)
                    f.write(temp+"\n")
                    

# getting links of two sub sub links
for a in soup.find_all('a', href=True):
    if("?" in a['href'] or "galco" in a['href'] or "with-confidence" in a['href']):
        continue
    else:
        if ("/shop" in a['href'] or "/get" in a['href']):
            temp = base_url1 + a['href']
            # cat = categories
            if temp not in url_list_cat:
                if(temp == "https://www.galco.com/get/Wrenches-Sockets-and-Ratchets" or temp == "https://www.galco.com/get/Driver-Tools"):
                    get_url(temp)
                else:
                    url_list_cat.append(temp)
                    f.write(temp+"\n")

f.close()
page.close()
