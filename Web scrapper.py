from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import pandas as pd


results = []
def item_info(str):
    ######### starting site request
    df = pd.DataFrame(results, columns = ['URL','Item No','Manfactuer No','Description','Price','Price in Volumes','Brand','Category','Subcategory','Series','UPC'])
    site= str
    hdr = {'User-Agent': 'chrome/5.0'}
    #requesting connection to the page
    req = Request(site,headers=hdr)
    page = urlopen(req)
    soup = BeautifulSoup(page,"html.parser")
    #######  required information  ############ 
    item_no ="" 
    Mft_no =""
    series =""
    price = ""
    price_in_volume = ""
    category =""
    subcategory =""
    description =""
    brand =""
    upc = ""
    #############  price   ################
    priceText = soup.find("div","col-xs-12 price priceDiv")
    if(priceText is not None):
        price = "$ "+priceText.text.strip()
    else:
        price=""
    ########### prices in volumes discounts #############
    s = []
    f = []
    piv = ""
    price_volume_div = soup.find("div", { "class" : "col-xs-10 col-md-12 productPrices" })
    if(price_volume_div is not None):
        price_eligible_div = price_volume_div.findAll("div",{"class":"col-xs-12"})
        for i in price_eligible_div:
            s = i.text.strip()
            f = s.splitlines()
        for i in range(len(f)):
            if(f[i] == ''):
                pass
            else:
                if(f[i]=="$"):
                    piv = piv +f[i]
                else:
                    piv = piv + f[i] + " "
        s = " ".join(piv.split())
        price_in_volume = s.replace("$","= $")     
    #########  price Currency  ############
    
    curr = soup.findAll('meta',property="og:content")
    for i in curr:
        print(i)
        
    ##########    Descripttion   ##########
    
    des = soup.findAll("div",{"id":"overview"})
    product_description = ''
    for i in des:
        parse_tag = i.findAll("p")
        temp1 = parse_tag[2].text.strip()
        strip_desc = temp1.split()
        temp2 = " "
        pro_desc = strip_desc[3:]
        #final prodcut description
        product_description = temp2.join(pro_desc)
    if(product_description == ''):
        for i in des:
            parse_tag = i.findAll("p")
            product_description = parse_tag[3].text.strip() 
    description = product_description 
    ########## item number ##############

    itm = soup.find("div","row productNumber")
    item_no = itm.span.text

    ############## Series | manufacNo | UPC   ################
    
    for spanItem in soup.findAll('span',itemprop=True):
        if("model" in spanItem['itemprop']):
            series = spanItem.text.strip()
        if(series == ''):
            series = "N/A"
        if("mpn" in spanItem['itemprop']):
            Mft_no = spanItem.text.strip()
        if("gtin" in spanItem['itemprop']):
            upc = spanItem.text.strip()
        if(upc == ''):
            upc = "N/A"
    ############ Category     #####################
    s = soup.findAll("div",{"class":"breadcrumbtrail"})
    first_child = soup.find("body").find("ol")
    category = first_child.findChildren()[10].text 
    ############   Sub Category   #################
    subcategory = first_child.findChildren()[13].text
    ############   Brand   #################
    br = soup.find("div",id="overview")
    temp_brand = br.find("p")
    brand = temp_brand.text.strip()
    ######################################
    
    results.append((site.strip(),item_no,Mft_no,description,price,price_in_volume,brand,category,subcategory,series,upc,))
    print(item_no)
    df.to_csv('products.csv', index = False,encoding='utf-8')
fp = open("products_links.txt","r")
link = fp.readline()
while link:
    item_info(link)
    link = fp.readline()






