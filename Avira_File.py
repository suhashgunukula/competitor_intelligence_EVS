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


Website_links = ['https://www.avira.com/en/buy-antivirus', 'https://www.avira.com/fr/buy-antivirus',
                 'https://www.avira.com/de/buy-antivirus']
Website_Location = ['USA', 'France','Germany']
#option = Options()
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = '/usr/bin/google-chrome'
driver = webdriver.Chrome(executable_path='D:\competitor_intelligence_EVS_1\chromedriver.exe', chrome_options=chrome_options)
#driver = webdriver.Chrome(options=option, executable_path="D:\selenium_automation\chromedriver.exe")
driver.maximize_window()
title = []
current_price = []
ac_renewal_price = []
years = []
devices = []
discount = []
website = []
Location = []
length = len(Website_links)
print(length)
for i in range(0,1):#length):
    baseurl = Website_links[i]
    # print(Website_links[i],i)
    # products_code[0]
    driver.get(baseurl)
    time.sleep(3)
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")

    ids = driver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        # print ii.tag_name
        print(ii.get_attribute('id'))
    time.sleep(2)
    id = []
    for a in range(0, len(ids)):
        v = ids[a].get_attribute('id')
        id.append(v)
    id
    len(id)
    id[0]
    # extracting the text consists of combobox from the above list using regex
    # this helps us to extract the id of the close button for every product
    id_required = []
    for pl in id:
        d = re.findall(r'subsWidgetModal-[0-9]+', pl) #
        if len(d) > 0:  # used to drop all the null values
            id_required.append(d)
        print(d)
    id_required  # finally we got the required combobox ids
    print(len(id_required))
    # converting nested list to normal list
    id_required = [element for innerList in id_required for element in
                   innerList]  # to convert nested lists to a flatlist
    id_required

    '''
    this helps us to extract the Devices filter
    '''
    id_required_1 = []
    for pl in id:
        d = re.findall(r'select-devices-no-brick[0-9]+', pl)
        if len(d) > 0:  # used to drop all the null values
            id_required_1.append(d)
        print(d)
    id_required_1  # finally we got the required combobox ids
    print(len(id_required_1))
    # converting nested list to normal list
    id_required_1 = [element for innerList in id_required_1 for element in
                     innerList]  # to convert nested lists to a flatlist
    id_required_1

    '''
        this helps us to extract the id of the each product which need to be clicked to entre the new window (see plans)
        '''
    id_required_2 = []
    for pl in id:
        d = re.findall(r'mo-qa-sl9productpillars-[0-9]+', pl)
        if len(d) > 0:  # used to drop all the null values
            id_required_2.append(d)
        print(d)
    id_required_2  # finally we got the required combobox ids
    print(len(id_required_2))
    # converting nested list to normal list
    id_required_2 = [element for innerList in id_required_2 for element in innerList]  # to convert nested lists to a flatlist
    id_required_2
    #time.sleep(2)
    # for products radio buttons
    id_required_3 = []
    for pl in id:
        d = re.findall(r'runtimes-list-brick[0-9]+', pl)
        if len(d) > 0:  # used to drop all the null values
            id_required_3.append(d)
        print(d)
    id_required_3  # finally we got the required combobox ids
    print(len(id_required_3))
    # converting nested list to normal list
    id_required_3 = [element for innerList in id_required_3 for element in innerList]  # to convert nested lists to a flatlist
    id_required_3

    length_id_required =len(id_required)
    length_id_required_1 = len(id_required_1)
    length_id_required_2 = len(id_required_2)
    length_id_required_3 = len(id_required_3)
    print(length_id_required,length_id_required_1,length_id_required_2,length_id_required_3)
    for j in range(0,length_id_required):
        '''
        Road map (outline): 
        url--> navigate to the position--> click on tarrifc plans --> new window opens click on one of the radio button to avoid loading randomly
        incase we have devices filter Take the count of the the drop down list items -->
        after completion close nd move to other product by simply clicking the right navigation arrow..
        '''

# step - 1
    # scroll down to the specific location
        element = driver.find_element_by_xpath("//*[@id='"+str(id_required_2[j])+"']")
        desired_y = (element.size['height'] / 2) + element.location['y']
        window_h = driver.execute_script('return window.innerHeight')
        window_y = driver.execute_script('return window.pageYOffset')
        current_y = (window_h / 2) + window_y
        scroll_y_by = desired_y - current_y
        scroll_y_by

        driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)

        '''
        Title:
        '''
        title_pro = driver.find_element_by_xpath("//*[@id='mainContent']/div[5]/div[2]/div[2]/div/div/div/div/div["+str(j+1)+"]/div/div/div[2]/h3")
        print(title_pro.text) #//*[@id="mainContent"]/div[5]/div[2]/div[2]/div/div/div/div/""""div[2]""""/div/div/div[2]/h3 # iteratable element
        f=str(title_pro.text)
        #title.append(title_pro.text)
        len(title)
        #title
        #for pl in title_pro:
            #print(pl.text)
        time.sleep(2)
        '''
        Pricing plan
        '''#//*[@id="mo-qa-sl9productpillars-1"]
        price_details=driver.find_element_by_xpath("//*[@id='"+str(id_required_2[j])+"']").click()
        time.sleep(2)
    #radio button click
    #radio_click = driver.find_element_by_xpath("//*[@id='runtimes-list-brick6']/li[1]/div[1]/label/span").click() # worked
        radio_click = driver.find_element_by_xpath("//*[@id='"+str(id_required_3[j])+"']/li[1]/div[1]/label/span").click() # worked

        Num_dev = driver.find_elements_by_xpath("//*[@id='"+str(id_required_1[j])+"']")
        len(Num_dev)
    # the below code is use to split the single line to numtiple to get the count
        '''
        from here --> ['1 Device\n3 Devices\n5 Devices']
        to here --> [['1 Device', '3 Devices', '5 Devices']]
        '''
        num_1= [tag.text.split("\n") for tag in Num_dev] # worked
        print(num_1)
        len(num_1)
        len(num_1[0])
        #devices.append(num_1[0])
        length_dev=len(num_1[0])
        print(length_dev)
        #print(length_dev)

        time.sleep(1)
    # selecting diff options
    #//*[@id="select-devices-no-brick6"]/option[1]
        #try:
            #option_selection = driver.find_element_by_xpath("//*[@id='" + str(id_required_1[j]) + "']/option[1]").click()  # option[1] this is iteratable element # worked
        #except NoSuchElementException:
            #print("exception handled")
        try:
            option_selection = driver.find_element_by_xpath("//*[@id='" + str(id_required_1[j]) + "']/option[1]").click()  # option[1] this is iteratable element # worked
            for t in range(0,length_dev):
                option_selection = driver.find_element_by_xpath("//*[@id='" + str(id_required_1[j]) + "']/option["+str(t+1)+"]").click()  # option[1] this is iteratable element # worked
                radio_click = driver.find_element_by_xpath("//*[@id='" + str(id_required_3[j]) + "']/li[2]/div[1]/label/span").click()  # li[2] this is iteratable element # worked

                time.sleep(2)

                duration_details = driver.find_elements_by_xpath("//*[@id='" + str(id_required_3[j]) + "']/li/div[1]")
                duration_details
                len(duration_details)
                for z1 in range(0, len(duration_details)):
                    v = duration_details[z1].text
                    years.append(v)
                for pl in duration_details:
                    print(pl.text)
                price_details = driver.find_elements_by_xpath("//*[@id='" + str(id_required_3[j]) + "']/li/div[2]")
                price_details
                len(price_details)
                for z in range(0, len(price_details)):
                    v = price_details[z].text
                    current_price.append(v)
                for pl in price_details:
                    print(pl.text)

                new_list = []
                new_list.extend([f for k in range(len(price_details))])
                print(new_list)

                title.append(new_list)

                new_list_dev = []
                dev=num_1[0][t]
                new_list_dev.extend(dev for h in range(len(price_details)))
                print(new_list_dev)

                devices.append(new_list_dev)
                #devices.append(num_1[0][t] * len(price_details))
                website.append([Website_links[i]] * len(price_details))
                website
                Location.append([Website_Location[i]] * len(price_details))
                Location
                time.sleep(2)
        except:
            #time.sleep(2)
            radio_click = driver.find_element_by_xpath("//*[@id='" + str(id_required_3[j]) + "']/li[2]/div[1]/label/span").click()  # li[2] this is iteratable element # worked

            time.sleep(1)

            duration_details = driver.find_elements_by_xpath("//*[@id='" + str(id_required_3[j]) + "']/li/div[1]")
            duration_details
            len(duration_details)
            for z1 in range(0, len(duration_details)):
                v = duration_details[z1].text
                years.append(v)
            for pl in duration_details:
                print(pl.text)
            price_details = driver.find_elements_by_xpath("//*[@id='" + str(id_required_3[j]) + "']/li/div[2]")
            price_details
            len(price_details)
            for z in range(0, len(price_details)):
                v = price_details[z].text
                current_price.append(v)
            for pl in price_details:
                print(pl.text)

            new_list = []
            new_list.extend([f for k in range(len(price_details))])
            print(new_list)

            title.append(new_list)
            #title.append(f * len(price_details))
            new_list_dev = []
            dev = num_1[0]
            new_list_dev.extend([dev for l in range(len(price_details))])
            print(new_list_dev)

            devices.append(new_list_dev)
            #devices.append(num_1[0] * len(price_details))
            website.append([Website_links[i]] * len(price_details))
            website
            Location.append([Website_Location[i]] * len(price_details))
            Location
            time.sleep(2)
            print("Fi")

        for close in range(0, length_id_required):
            try:
                close = driver.find_element_by_xpath("//*[@id='" + str(id_required[close]) + "']/button").click()
            except:
                print(close, "not worked")

        # right navigation arrow
        nav = driver.find_element_by_xpath("//*[@id='mainContent']/div[5]/div[2]/div[2]/div/div/i[2]").click()
        time.sleep(2)

f
emp=[]
emp.insert(len(emp),f)
emp
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
years
len(years)
website = [element for innerList in website for element in innerList]  # to convert nested lists to a flatlist
website
Location = [element for innerList in Location for element in innerList]  # to convert nested lists to a flatlist
Location
title = [element for innerList in title for element in innerList]  # to convert nested lists to a flatlist
title
devices = [element for innerList in devices for element in innerList]  # to convert nested lists to a flatlist
devices



# creating a dataframe
dist_1 = pd.DataFrame()
dist_1['S.no'] = list(range(0, len(current_price)))
dist_1['date'] = date.today().strftime("%d/%m/%Y")
dist_1['Date'] = int(date.today().strftime("%d"))
dist_1['Month'] = int(date.today().strftime("%m"))
dist_1['Year'] = int(date.today().strftime("%y"))
dist_1['title'] = pd.Series(title)
dist_1['current_price'] = pd.Series(current_price)
# to replace the unneccesary values in the column of a dataframe
dist_1['current_price'] = dist_1['current_price'].str.replace("*", "")
# to replace the unneccesary values in the column of a dataframe
dist_1['current_price'] = dist_1['current_price'].str.replace("\u200b", "")

dist_1['Actual_price/Renewal'] = pd.Series(ac_renewal_price)
# dist_1['years']=pd.Series(years)
# dist_1['discount']=pd.Series(discount)
dist_1['Devices'] = pd.Series(devices)
for q in range(0,len(dist_1['current_price'])):
    dist_1['Devices'][q]= str(devices[q])+" / "+str(years[q])

dist_1['Location'] = pd.Series(Location)
dist_1['website'] = pd.Series(website)
dist_1['Description']=""
# dist_1.set_index(lst)
dist_1.describe()  # to describe the data mean median percentiles
dist_1.info
dist_1.dtypes  # to check the data types of the column
data=dist_1
'''
dist_1.to_excel("C:\\Users\\HP\\Desktop\\EVS webscrapping pricing tracker\\Avira_" + str(date.today().strftime("%y")) + "_" + str(date.today().strftime("%d")) + ".xlsx", index=None)
# here im directly appending the data frame to a excel file
'''

driver.close()






