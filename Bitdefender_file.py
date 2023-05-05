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
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

Website_links = ['https://www.bitdefender.co.uk/solutions/', 'https://www.bitdefender.fr/solutions/',
                  'https://www.bitdefender.com.br/solutions/','https://www.bitdefender.com/solutions/',
                 'https://www.bitdefender.de/solutions/',]
Website_Location = ['UK', 'France', 'Brasil', 'USA','Germany']
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
#observation:
#germany website differs
#usa website differs

for i in range(0, len(Website_links)):
    baseurl = Website_links[i]
    # print(Website_links[i],i)
    # products_code[0]
    driver.get(baseurl)

    # explicit wait
    #timeout = 5
    #try:
        #element_present = EC.presence_of_element_located((By.CLASS_NAME, 'heading-3'))
        #WebDriverWait(driver, timeout).until(element_present)
    #except TimeoutException:
        #print("Timed out waiting for page to load")
    #finally:
        #print("Page loaded")
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    driver.execute_script("window.scrollTo(0,1000)")
    if i ==4:
        #html = driver.page_source
        #soup = BeautifulSoup(html, "lxml")

        title_1 = soup.find_all("h3", {"class": "productS__title"})
        title_1
        len(title_1)
        for j in range(0, len(title_1)):
            v = title_1[j].text
            title.append(v)
        for pl in title_1:
            print(pl.text)
        website.append([Website_links[i]] * len(title_1))
        website
        Location.append([Website_Location[i]] * len(title_1))
        Location
    # devices
    # under-title pb-2
        title_1_dev = soup.find_all("span", {"class": "solutions__testDevices"})
        title_1_dev
        len(title_1_dev)
        for k in range(0, len(title_1_dev)):
            v = title_1_dev[k].text
            devices.append(v)
        #incase if there is any null values we use insert function to insert 'NA' in the empty spaces
        if len(title_1)!=len(title_1_dev):
            for x in range(0, (len(title_1) - len(title_1_dev))):
                devices.insert(len(devices) + x, 'NA')
        for pl in title_1_dev:
            print(pl.text)
    # price
    # new-price
        title_1_pri = soup.find_all("div", {"class": "productS__disc"})
        title_1_pri
        len(title_1_pri)
        l1=[]
        l2=[]
        for l in range(0, len(title_1_pri)):
            v = title_1_pri[l].text.replace("\n ", '').strip().split(" ")[0]
            f = title_1_pri[l].text.replace("\n", '').strip().split(" ")[2].replace("SPAREN","")
            l1.append(f)
            l2.append(v)
            current_price.append(f)
            ac_renewal_price.append(v)
            l1
            l2
        time.sleep(2)


    else:

#top row titles
        title_1=soup.find_all("h3",{"class":"heading-3"})
        title_1
        len(title_1)
        for a in range(0, len(title_1)):
            v = title_1[a].text
            title.append(v)
        for pl in title_1:
            print(pl.text)
        website.append([Website_links[i]] * len(title_1))
        website
        Location.append([Website_Location[i]] * len(title_1))
        Location

# Top row devices
    #under-title pb-2
        title_1_dev = soup.find_all("h4", {"class": "under-title pb-2"})
        title_1_dev
        len(title_1_dev)
        for b in range(0, len(title_1_dev)):
            v = title_1_dev[b].text
            devices.append(v)
        #incase if there is any null values we use insert function to insert 'NA' in the empty spaces
        if len(title_1)!=len(title_1_dev):
            for x in range(0, (len(title_1) - len(title_1_dev))):
                devices.insert(len(devices) + x, 'NA')
        devices
        for pl in title_1_dev:
            print(pl.text)
# Top row price
    #new-price
        title_1_pri = soup.find_all("div", {"class": "new-price"})
        title_1_pri
        len(title_1_pri)
        for c in range(0, len(title_1_pri)):
            v = title_1_pri[c].text
            current_price.append(v)

        for pl in title_1_pri:
            print(pl.text)
# Top row Actual price
    # old-price
        title_1_pri_old = soup.find_all("div", {"class": "old-price"})
        title_1_pri_old
        len(title_1_pri_old)
        for d in range(0, len(title_1_pri_old)):
            v = title_1_pri_old[d].text
            ac_renewal_price.append(v)
        for pl in title_1_pri_old:
            print(pl.text)

# next set of products other than top row

        title_2 = soup.find_all("h4", {"class": "mb-3 title we-row we-justify-content-center"})
        title_2
        len(title_2)
        for e in range(0, len(title_2)):
            v = title_2[e].text
            title.append(v)

        for pl in title_2:
            print(pl.text)
        website.append([Website_links[i]] * len(title_2))
        website
        Location.append([Website_Location[i]] * len(title_2))
        Location

# next set of products devices other than top row

    # under-title pb-2
        title_2_dev = soup.find_all("p", {"class": "we-row mb-2 p-0 we-justify-content-center"})
        title_2_dev
        len(title_2_dev)
        for f in range(0, len(title_2_dev)):
            v = title_2_dev[f].text
            devices.append(v)
        #if len(title_2)!=len(title_2_dev):
            #devices.insert(len(title_2_dev) + (len(title_2)-len(title_2_dev)), 'NA')

        for pl in title_2_dev:
            print(pl.text)

# # next set of products price other than top row
    # p-0 m-0
        title_2_pri = soup.find_all("span", {"class": "p-0 m-0"})
        title_2_pri
        len(title_2_pri)
        for g in range(0, len(title_2_pri)):
            v = title_2_pri[g].text
            current_price.append(v)

        for pl in title_2_pri:
            print(pl.text)
# next set of products Actual price other than top row
    # old-price p-0 m-0
        title_2_pri_old = soup.find_all("del", {"class": "old-price p-0 m-0"})
        title_2_pri_old
        len(title_2_pri_old)
        for h in range(0, len(title_2_pri_old)):
            v = title_2_pri_old[h].text
            ac_renewal_price.append(v)
        for pl in title_2_pri_old:
            print(pl.text)


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
    dist_1['Number of Devices_1'][i] = ''.join(dist_1['Devices'][i]).replace("/ 1 Jahr",' ').replace("1 Jahr /",' ')
dist_1['Number of Devices'] = dist_1['Number of Devices_1'].astype('str').str.extractall('(\d+)').unstack().fillna('').sum(axis=1).astype(int)
# to treat the devices data
dist_1.loc[dist_1['Number of Devices'].isnull(),'No of Devices'] = 'NA'
dist_1.loc[dist_1['Number of Devices'].notnull(), 'No of Devices'] = dist_1['Number of Devices']

dist_1['Location']=pd.Series(Location)
dist_1['website']=pd.Series(website)

#dist_1.set_index(lst)
dist_1.describe() # to describe the data mean median percentiles
dist_1.info
dist_1.dtypes # to check the data types of the column

data=dist_1
#Downloads


data.to_excel("Downloads"+str(date.today())+"-"+".xlsx")
'''
dist_1.to_excel("C:\\Users\\HP\\Desktop\\EVS webscrapping pricing tracker\\Bitdefender_"+str(date.today().strftime("%y"))+"_"+str(date.today().strftime("%d"))+".xlsx", index=None)
    #here im directly appending the data frame to a excel file
'''