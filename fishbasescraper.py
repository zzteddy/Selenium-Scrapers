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
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import csv



def check_exists_by_text(text):
    if text not in driver.page_source :
        return False
    return True

#login info
username = 'edted24@gmail.com'
password = 'catchbass'

#Login to facbook

driver = webdriver.Firefox() 

driver.get('https://www.fishbase.de') 
time.sleep(1) 


#intput query
queryterm = 'Hemiramphus brasiliensis'




def geturlsfromterm(queryterm):
    driver.get('https://www.fishbase.de') 
    time.sleep(1) 
    searchbar = driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/form/p[2]/span[2]/input')
    searchbar.send_keys(queryterm)
    searchbar.submit() 
    #navigate to photos
    time.sleep(2) 
    #driver.find_element_by_xpath('//span[contains(.,"Pictures")]').click()
    driver.find_element_by_xpath('//a[contains(text(),"Pictures")]').click()

    time.sleep(1) 
    #driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td[1]/a[1]/span/img').click()
    action = ActionChains(driver)
    # move to element operation
    hoverover =  driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td[1]')
    action.move_to_element(hoverover).perform()
    #action.moveByOffset​(200,100)
    WebDriverWait(driver, 1000000).until(EC.element_to_be_clickable((By.XPATH, '/html/body/table[1]/tbody/tr[2]/td[1]/a[1]/span/img'))).click()

    urls=[]
    wait = WebDriverWait(driver, 3)
    while True:
        # grab the data
        if not check_exists_by_text("gif"):
            
            image=driver.find_element_by_xpath('//img[@alt=\"' + queryterm + '\"]')
            
            #image = driver.find_elements_by_tag_name('img')
            if type(image) == list :
                url = image[1].get_attribute('src') 
            else:
                url = image.get_attribute('src')

            location = driver.find_element_by_xpath("//tr[2]/td[2]").text
            urls.append((url,location))

        # click next link
        try:
            element = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(.,"Next page»")]')))
            element.click()
        except TimeoutException:
            break


    with open(queryterm+'.csv','w', newline="") as out:
        csv_out=csv.writer(out)
        csv_out.writerow(['Scientific Name','Location'])
        for row in urls:
            csv_out.writerow(row)

queryterms=[]
f = open("species.txt", "r")
for x in f:
  queryterms.append(x.rstrip())
for x in range(271,281):
    print(queryterms[x])
    geturlsfromterm(queryterms[x])

driver.close()