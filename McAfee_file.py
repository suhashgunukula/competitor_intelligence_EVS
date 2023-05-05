import time
import pandas as pd
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import numpy as np
from datetime import date
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import re
import requests

Website_links = ['https://www.mcafee.com/en-gb/index.html', 'https://www.mcafee.com/fr-fr/index.html',
                 'https://www.mcafee.com/de-de/index.html', 'https://www.mcafee.com/pt-br/index.html',
                 'https://www.mcafee.com/en-in/index.html']
Website_Location = ['UK', 'France', 'Germany', 'Brasil', 'USA']
option = Options()
driver = webdriver.Chrome(options=option, executable_path="D:\selenium_automation\chromedriver.exe")
driver.maximize_window()
title = []
current_price = []
ac_renewal_price = []
years = []
devices = []
discount = []
website = []
Location = []

# Trying loop
for i in range(0, len(Website_links)):
    baseurl = Website_links[2]
    # print(Website_links[i],i)
    # products_code[0]
    driver.get(baseurl)

    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    # product names
    uk_pro = soup.find_all("div", {"class": "cmp-cardcontent"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    uk_pro

    uk_pro_1 = [tag.text.split(" ")[0] for tag in uk_pro]  # worked
    print(uk_pro_1)
    len(uk_pro_1)
    len(uk_pro_1[0])

    for y in range(0, len(uk_pro_1)):
        if len(uk_pro_1[y]) <= 9 and len(uk_pro_1[y]) > 1 and uk_pro_1[y] != 'Support' and uk_pro_1[y] != 'Features' and uk_pro_1[y] != 'How' and uk_pro_1[y] != 'Apple' and uk_pro_1[y] != 'Hybrid' and uk_pro_1[y] != 'Resources' and uk_pro_1[y] != 'About':
            v = uk_pro_1[y].replace(" ", '').strip()
            title.append(v)
    title
    len(title)
    # price details
    uk_pri = soup.find_all("div", {"class": "cmp-card__btn price-section"})  ##worked for price
    uk_pri
    uk_pri_1 = [tag.text.split(" ")[0] for tag in uk_pri]  # worked
    print(uk_pri_1)
    len(uk_pri_1)
    current_price_uk = uk_pri_1
    current_price_uk

    website.append([Website_links[i]] * len(uk_pri_1))
    website
    Location.append([Website_Location[i]] * len(uk_pri_1))
    Location

    uk_ac_pri = soup.find_all("div", {"class": "cmp-card__btn price-section"})  ##worked for price
    uk_ac_pri

    for z in range(0, len(uk_ac_pri)):
        v = uk_ac_pri[z].text.split(" ")[3]
        ac_renewal_price.append(v)
    ac_renewal_price
    len(ac_renewal_price)
    # devices details
    uk_devices = soup.find_all("li", {"class": "fw-400"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    uk_devices
    len(uk_devices)
    uk_devices_1 = [tag.text.split(" ")[0] for tag in uk_devices]  # worked
    print(uk_devices_1)
    len(uk_devices_1)
    dev_e = []
    for t in range(0, len(uk_devices_1)):
        if uk_devices_1[t] != 'Full-service' and uk_devices_1[t] != 'Scans':
            v = uk_devices_1[t].replace(" ", '').strip()
            dev_e.append(v)
            dev_e
        odd_i = []
        even_i = []
        for q in range(0, len(dev_e)):
            if q % 2:
                even_i.append(dev_e[q])
            else:
                odd_i.append(dev_e[q])
    odd_i
    even_i
    devices = even_i
    devices
    # len(devices)

    #for website 2  fr

    # product names
    fr_pro = soup.find_all("div", {"class": "cmp-cardcontent"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    fr_pro

    fr_pro_1 = [tag.text.split(" ")[0] for tag in fr_pro]  # worked
    print(fr_pro_1)
    len(fr_pro_1)
    len(fr_pro_1[0])

    for y in range(0, len(fr_pro_1)):
        if len(fr_pro_1[y]) <= 9 and len(fr_pro_1[y]) > 1 and fr_pro_1[y] != 'Support' and fr_pro_1[y] != 'Features' and \
                fr_pro_1[y] != 'How' and fr_pro_1[y] != 'Apple' and fr_pro_1[y] != 'Hybrid' and fr_pro_1[
            y] != 'Resources' and fr_pro_1[y] != 'About':
            v = fr_pro_1[y].replace(" ", '').strip()
            title.append(v)
    title
    len(title)

    fr_pri = soup.find_all("div",{"class": "cmp-card__btn price-section"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    fr_pri
    len(fr_pri)
    for w in range(0, len(fr_pri)):
        v = fr_pri[w].text.replace(" ", '').strip().split(" ")[0]
        current_price.append(v)
    current_price

    fr_devices = soup.find_all("li", {"class": "fw-400"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    fr_devices
    len(fr_devices)
    fr_devices_1 = [tag.text.split(" ")[0] for tag in fr_devices]  # worked
    print(fr_devices_1)
    len(fr_devices_1)
    dev_fr = []
    for t in range(0, len(fr_devices_1)):
        if fr_devices_1[t] != 'Full-service' and fr_devices_1[t] != 'Scans':
            v = fr_devices_1[t].replace(" ", '').strip()
            dev_fr.append(v)
            dev_fr
        odd_i = []
        even_i = []
        for q in range(0, len(dev_fr)):
            if q % 2:
                even_i.append(dev_fr[q])
            else:
                odd_i.append(dev_fr[q])

    odd_i
    even_i
    devices = even_i
    devices
###### fro website 3

    # for website de
    de_pro = soup.find_all("div", {"class": "cmp-cardcontent"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    de_pro

    de_pro_1 = [tag.text.split(" ")[0] for tag in de_pro]  # worked
    print(de_pro_1)
    len(de_pro_1)
    len(de_pro_1[0])
    title_de=[]
    for y in range(0, len(de_pro_1)):

        if len(de_pro_1[y]) <= 9 and len(de_pro_1[y]) > 1 and de_pro_1[y] != 'Support' and de_pro_1[y] != 'Features' and \
                de_pro_1[y] != 'How' and de_pro_1[y] != 'Funktionen' and de_pro_1[
            y] != 'Ressourcen' and de_pro_1[y] != 'Info':
            v = de_pro_1[y].replace(" ", '').strip()
            title_de.append(v)
    title_de.insert(3,"Advanced")
    title_de.insert(6, "Advanced")
    title_de
    title = title + title_de
    len(title)

    de_pri = soup.find_all("div",{"class": "cmp-card__btn price-section"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    de_pri
    len(fr_pri)
    for w in range(0, len(de_pri)):
        v = de_pri[w].text.replace(" ", '').strip().split(" ")[0]
        current_price.append(v)
    current_price

    de_devices = soup.find_all("li", {"class": "fw-400"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    de_devices
    len(de_devices)
    de_devices_1 = [tag.text.split(" ")[0:4] for tag in de_devices]  # worked
    print(de_devices_1)
    len(de_devices_1)
    dev_de = []
    for t in range(0, len(de_devices_1)):
        if de_devices_1[t] != 'Full-service' and de_devices_1[t] != 'Scans':
            v = de_devices_1[t]
            dev_de.append(v)
            dev_de
        odd_i = []
        even_i = []
        for q in range(0, len(dev_de)):
            if q % 2:
                even_i.append(dev_de[q])
            else:
                odd_i.append(dev_de[q])

    odd_i
    even_i
    len(even_i)
    devices = even_i
    devices.extend(even_i)
    devices


########### for website 4

#for website br
    br_pro = soup.find_all("div", {"class": "cmp-text block-card text-center"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    br_pro

    br_pro_1 = [tag.text.split(" ")[0] for tag in br_pro]  # worked
    print(br_pro_1)
    len(br_pro_1)
    len(br_pro_1[0])
    title_br = []
    for y in range(0, len(br_pro)):

        v = br_pro_1[y].replace(" ", '').strip().split(" ")[0]
        #v = br_pro_1[y].replace(" ", '').strip()
        title_br.append(v)
    title_br

    br_pri = soup.find_all("p",{"class":"fs-15"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    br_pri
    len(br_pri)
    cu_P=[]
    for w in range(0, len(br_pri)):
        v = br_pri[w].text.replace(" ", '').strip().split(" ")[0]
        cu_P.append(v)
    cu_P
    current_price

    ac_price = soup.find_all("p",{"class": "fs-36 price-fallback-font"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    ac_price
    for pl in ac_price:
        print(pl.text)
    ac_P = []
    for w in range(0, len(ac_price)):
        v = ac_price[w].text.replace(" ", '').strip().split(" ")[0]
        ac_P.append(v)
    ac_P

    br_dev = soup.find_all("span", {"style": "font-weight: bold;"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    br_dev
    len(br_dev)
    for pl in br_dev:
        print(pl.text)
    br_dev_1 = []
    for w in range(0, len(br_dev)):
        v = br_dev[w].text.replace(" ", '').strip().split(" ")[0]
        br_dev_1.append(v)
    br_dev_1
    len(br_dev_1)

######### for website usa
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    usa_pro = soup.find_all("div", {"class": "cmp-text block-card text-center"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    usa_pro

    usa_pro_1 = [tag.text.split(" ")[0] for tag in usa_pro]  # worked
    print(usa_pro_1)
    len(usa_pro_1)
    len(usa_pro_1[0])
    title_usa = []
    for y in range(0, len(usa_pro)):
        v = usa_pro_1[y].replace(" ", '').strip().split(" ")[0]
        # v = br_pro_1[y].replace(" ", '').strip()
        title_usa.append(v)
    title_usa

    usa_pri = soup.find_all("p", {"class": "fs-15"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    usa_pri
    len(usa_pri)
    usa_cu_P = []
    for w in range(0, len(usa_pri)):
        v = usa_pri[w].text.replace(" ", '').strip().split(" ")[0]
        usa_cu_P.append(v)
    usa_cu_P
    current_price

    usa_ac_price = soup.find_all("p",{"class": "fs-36 price-fallback-font"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    usa_ac_price
    for pl in usa_ac_price:
        print(pl.text)
    usa_ac_P = []
    for w in range(0, len(usa_ac_price)):
        v = usa_ac_price[w].text.replace(" ", '').strip().split(" ")[0]
        usa_ac_P.append(v)
    usa_ac_P

    usa_dev = soup.find_all("span", {"style": "font-weight: bold;"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
    usa_dev
    len(usa_dev)
    for pl in usa_dev:
        print(pl.text)
    usa_dev_1 = []
    for w in range(0, len(usa_dev)):
        v = usa_dev[w].text.replace(" ", '').strip().split(" ")[0]
        usa_dev_1.append(v)
    usa_dev_1
    len(usa_dev_1)
####################################################################################################################
import time
import pandas as pd
import lxml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import numpy as np
from datetime import date
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import re
import requests

Website_links = ['https://www.mcafee.com/en-gb/index.html', 'https://www.mcafee.com/fr-fr/index.html',
                 'https://www.mcafee.com/de-de/index.html', 'https://www.mcafee.com/pt-br/index.html',
                 'https://www.mcafee.com/en-in/index.html']
Website_Location = ['UK', 'France', 'Germany', 'Brasil', 'USA']
option = Options()
driver = webdriver.Chrome(options=option, executable_path="D:\selenium_automation\chromedriver.exe")
driver.maximize_window()
title = []
current_price = []
ac_renewal_price = []
years = []
devices = []
discount = []
website = []
Location = []

# Trying loop
for i in range(0, len(Website_links)):
    baseurl = Website_links[i]
    # print(Website_links[i],i)
    # products_code[0]
    driver.get(baseurl)
    time.sleep(4)
# every time the loop runs the html and soup need to be scraped to get the current page
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
# condition for the web links are from these postions then run the case or else pass to else condition
    if i in (0,2,1): #in range(start,stop,increment by)
        # product names
        pro = soup.find_all("div", {"class": "cmp-cardcontent"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
        pro
#spliting the text from the tags
        pro_1 = [tag.text.split(" ")[0] for tag in pro]  # worked
        # tag --> extract the text from tag using text function --> split the extracted text by delimiter space using function split(' ')
        # ---> then get the [0] position of every text using a loop
        print(pro_1)
        len(pro_1)
        len(pro_1[0])
#here i have used the condition because the Germany site not allowing me to scarpe all the title of products
# so i have inserted the missing titles using the function below
        if i ==2:
            title_de = []
            for l in range(0, len(pro_1)):

                if len(pro_1[l]) <= 9 and len(pro_1[l]) > 1 and pro_1[l] != 'Support' and pro_1[l] != 'Features' and pro_1[l] != 'How' and pro_1[l] != 'Funktionen' and pro_1[l] != 'Ressourcen' and pro_1[l] != 'Info':
                    v = pro_1[l].replace(" ", '').strip()
                    title_de.append(v)
            title_de.insert(3, "Advanced")
            title_de.insert(6, "Advanced")
            title_de
            title.extend(title_de)
        else:

            for y in range(0, len(pro_1)):
                if len(pro_1[y]) <= 9 and len(pro_1[y]) > 1 and pro_1[y] != 'Support' and pro_1[y] != 'Features' and pro_1[y] != 'How' and pro_1[y] != 'Apple' and pro_1[y] != 'Hybrid' and pro_1[y] != 'Resources' and pro_1[y] != 'About':
                    v = pro_1[y].replace(" ", '').strip()
                    title.append(v)
            title
            len(title)
        # price details
        pri = soup.find_all("div", {"class": "cmp-card__btn price-section"})  ##worked for price
        pri
        for x in range(0, len(pri)):
            v = pri[x].text.split(" ")[0]
            current_price.append(v)
        current_price
        len(current_price)
        pri_1 = [tag.text.split(" ")[0] for tag in pri]  # worked
        print(pri_1)
        len(pri_1)
        current_price_uk = pri_1
        current_price_uk
# writing website lnks and location to different columns based on the len of the above list
        website.append([Website_links[i]] * len(pri_1))
        website
        Location.append([Website_Location[i]] * len(pri_1))
        Location
# for actual price/renewal price
        ac_pri = soup.find_all("div", {"class": "cmp-card__btn price-section"})  ##worked for price
        ac_pri
        len(ac_pri)
        for z in range(0, len(ac_pri)):
            v = ac_pri[z].text.split(" ")[3]
            ac_renewal_price.append(v)
        ac_renewal_price
        len(ac_renewal_price)
#trying to put the condition if there is any null value (no values) then print 'NA' instead of null
# but here we have got the value one is '/n' and the second one is ""

        if len(ac_pri) == 0 and len(pri_1) == len(title): #this if condition will trigger only when the len is equal to 0
            for q in range(0, len(pri_1)):
                # 5
                ac_renewal_price.insert(len(ac_pri) + q, 'NA')  # worked #to add elemets from the index start
                # website.insert(len(discount)+q,Website_links[i])  # worked but kept hold
            # discount = with1__na + discount
        elif len(ac_pri) == 0 and len(pri_1) == 8:
            for w in range(0, 8):
                # 5
                ac_renewal_price.insert(len(ac_pri) + w, 'NA')

        # devices details
# for the devices data which the product support
        no_devices = soup.find_all("li", {"class": "fw-400"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
        no_devices
        len(no_devices)
        devices_1 = [tag.text.split(" ")[0:4] for tag in no_devices]  # worked # insted of [0] i have kept [0:4]
        print(devices_1)
        len(devices_1)
#here based on the tag we have got device licence+device data but we require only the device data so we have used the below technique
# it first get the data of licence+device for card 1 and move to card 2 and so on
# in this case the values scrapped in odd and even positons of list to get the required data i have used below step
#steps:
        #creating an empty list -----> remove if there is anyother data appere using if condition
        #creating two new empty lists namely(odd_i,even_i)
        #now write the logic to seperate all the even and odd into two lists
        dev_e = []
        for t in range(0, len(devices_1)):
            if devices_1[t] != ['Full-service'] and devices_1[t] != ['Scans']:
                v = devices_1[t]#.replace(" ", '').strip()
                dev_e.append(v)
                dev_e
            odd_i = []
            even_i = []
            for q in range(0, len(dev_e)):
                if q % 2:
                    even_i.append(dev_e[q])
                else:
                    odd_i.append(dev_e[q])
        devices.extend(even_i)
        devices
        odd_i
        even_i
        #devices = even_i
        #devices
    else:
#this condition only trigger if the value of i doesn't match to the first condition
    #if i in range(3,4,1):
        produc = soup.find_all("div",{"class": "cmp-text block-card text-center"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
        produc

        produc_1 = [tag.text.split(" ")[0] for tag in produc]  # worked
        print(produc_1)
        len(produc_1)
        len(produc_1[0])
        #title_produc = []
        for n in range(0, len(produc)):
            v = produc_1[n].replace(" ", '').strip().split(" ")[0]
            # v = br_pro_1[y].replace(" ", '').strip()
            #title_produc.append(v)
            title.append(v)
        #title_produc
        title

        usa_pri = soup.find_all("p", {"class": "fs-15"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
        usa_pri
        len(usa_pri)

        for u in range(0, len(usa_pri)):
            v = usa_pri[u].text.replace(" ", '').strip().split(" ")[0]
            #usa_cu_P.append(v)
            current_price.append(v)
        #usa_cu_P
        current_price
# writing website lnks and location to different columns based on the len of the above list
        website.append([Website_links[i]] * len(usa_pri))
        website
        Location.append([Website_Location[i]] * len(usa_pri))
        Location

# for actual price/renewal price
        usa_ac_price = soup.find_all("p", {"class": "fs-36 price-fallback-font"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
        usa_ac_price

        for g in range(0, len(usa_ac_price)):
            v = usa_ac_price[g].text.replace(" ", '').strip().split(" ")[0]
            #usa_ac_P.append(v)
            ac_renewal_price.append(v)
        ac_renewal_price

# for Devices data
        usa_dev = soup.find_all("span",{"style": "font-weight: bold;"})  # "p",{"class":"fs-15 mb-0"} ) #worked for price
        usa_dev
        len(usa_dev)

        for b in range(0, len(usa_dev)):
            v = usa_dev[b].text.replace(" ", '').strip().split(" ")[0]
            #usa_dev_1.append(v)
            devices.append(v)
        devices

title
len(title)
current_price
len(current_price)
ac_renewal_price
len(ac_renewal_price)
years
len(years)
devices
len(devices)
discount
len(discount)
website
len(website)
Location
len(Location)
website = [element for innerList in website for element in innerList] # to convert nested lists to a flatlist
website
Location = [element for innerList in Location for element in innerList] # to convert nested lists to a flatlist
Location

#creating a dataframe
dist_1=pd.DataFrame()
dist_1['S.no']=list(range(0, len(title)))
dist_1['date']=date.today().strftime("%d/%m/%Y")
dist_1['Date']=int(date.today().strftime("%d"))
dist_1['Month']=int(date.today().strftime("%m"))
dist_1['Year']=int(date.today().strftime("%y"))
dist_1['title']=pd.Series(title)
dist_1['current_price']=pd.Series(current_price)
# to replace the unneccesary values in the column of a dataframe
dist_1['current_price']=dist_1['current_price'].str.replace("*","")
# to replace the unneccesary values in the column of a dataframe
dist_1['current_price']=dist_1['current_price'].str.replace("\u200b","")

dist_1['Actual_price/Renewal']=pd.Series(ac_renewal_price)
#dist_1['years']=pd.Series(years)
#dist_1['discount']=pd.Series(discount)
dist_1['Devices']=pd.Series(devices)
#data processing for the column devices
dist_1['Number of Devices_1']=""
for i in range (0,len(dist_1['current_price'])):
    dist_1['Number of Devices_1'][i] = ''.join(dist_1['Devices'][i]).replace("\xa0",' ')
dist_1['Number of Devices'] = dist_1['Number of Devices_1'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
# to treat the devices data
dist_1.loc[dist_1['Number of Devices'].isnull(),'No of Devices'] = 'Unlimited'
dist_1.loc[dist_1['Number of Devices'].notnull(), 'No of Devices'] = dist_1['Number of Devices']

dist_1['Location']=pd.Series(Location)
dist_1['website']=pd.Series(website)

#dist_1.set_index(lst)
dist_1.describe() # to describe the data mean median percentiles
dist_1.info
dist_1.dtypes # to check the data types of the column
sum(dist_1['Year'])
dist_1.to_csv("C:\\Users\\HP\\Desktop\\EVS webscrapping pricing tracker\\norton.csv", index=None)
    #here im directly appending the data frame to a csv file
import openpyxl
import xlrd
dist_1.to_excel("C:\\Users\\HP\\Desktop\\EVS webscrapping pricing tracker\\McAfee_"+str(date.today().strftime("%y"))+"_"+str(date.today().strftime("%d"))+".xlsx", index=None)
    #here im directly appending the data frame to a excel file

devices[0]

current_price[0][0]
dist_1['current_price']

# to replace the unneccesary values in the column of a dataframe
dist_1['current_price']=dist_1['current_price'].str.replace("*","")
dist_1['Devices'][0]
#this is used to remove list in the column and
dist_1['Number of Devices_1']=""
for i in range (0,len(dist_1['current_price'])):
    dist_1['Number of Devices_1'][i] = ''.join(dist_1['Devices'][i]).replace("\xa0",' ')
dist_1['Number of Devices'] = dist_1['Number of Devices_1'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
dist_1.dtypes
dist_1['Number of Devices'][2].dtype

# to treat the devices data
dist_1.loc[dist_1['Number of Devices'].isnull(),'No of Devices'] = 'Unlimited'
dist_1.loc[dist_1['Number of Devices'].notnull(), 'No of Devices'] = dist_1['Number of Devices']

