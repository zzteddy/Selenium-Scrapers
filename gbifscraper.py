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
driver = webdriver.Firefox() 
driver.get('https://www.gbif.org/occurrence/search?occurrence_status=present&q=') 
time.sleep(1) 
queryterm = "Sarda sarda"
driver.find_element_by_xpath('//span[contains(.,"Scientific name")]').click()
query = driver.find_element_by_xpath('(//input[@type="text"])[3]')
query.send_keys(queryterm)
time.sleep(1)

actions = ActionChains(driver)
actions.send_keys(u'\ue007')
actions.perform()
time.sleep(1)
#driver.find_element_by_xpath('//li[2]/span').click()
driver.find_element_by_xpath('//a[contains(text(),"Gallery")]').click()
