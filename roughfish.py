from os import strerror
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import urllib
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import csv 

def check_exists_by_id(id):
    try:
        driver.find_element_by_id(id)
    except ElementNotInteractableException:
        return False
    return True


def check_exists_by_text(text):
    if text not in driver.page_source :
        return False
    return True


driver = webdriver.Firefox() 
driver.get('https://www.roughfish.com/fish-species-list') 
time.sleep(1) 


def scrape(queryterm):
    driver.get('https://www.roughfish.com/fish-species-list') 
    time.sleep(1) 
    urls=[]
    search = driver.find_element_by_name("field_scientific_name_value") 
    search.send_keys(queryterm)
    search.submit()
    time.sleep(1)

    
    try:
        driver.find_element_by_xpath("//td[4]/a").click()
        bool=True
        while(bool):
            images = driver.find_elements_by_tag_name('img')
            #if images.__sizeof__>2:
            for image in images:
                tempimg = str(image.get_attribute('src'))
                if "lifelist" in tempimg and tempimg not in urls:
                    ind = tempimg.index("?")
                    tempimg=tempimg[0:ind]
                    tempimg=tempimg.replace('/styles/thumbnail/public','')
                    print(tempimg)
                    urls.append(tempimg)
                       
            if check_exists_by_text("next"):
                driver.find_element_by_xpath("//a[contains(.,'next ›')]").click()
            else:
                bool = False
        with open(queryterm+'.csv','w', newline="") as out:
            csv_out=csv.writer(out)
            csv_out.writerow(['url',' '])
            for row in urls:
                csv_out.writerow([row," "])                
          
            
    except:
        return
        
        
queryterms=[]
doenalready=[10,11,18,24,32,45,46,47,51,56,57,64,66,67,68,73,75,79,81,82,86,101,102,103,108,110,111,112,115,120,121,128,131,132,138,143,150,151,152,155,157,161,165,168,169,172,173,175,177,180,181,183,194,202,203,209,213,221,223,227,228,236,241,243,245,246,248,249,251,252,253,261,263,266,269,270,271,276,279]
f = open("species2.txt", "r")
for x in f:
  queryterms.append(x.rstrip())
for x in range(0,280):
    if x not in doenalready:
        print(x)
        print(queryterms[x])
        scrape(queryterms[x])

