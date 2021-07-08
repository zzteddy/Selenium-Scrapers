import tkinter
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import urllib
import urllib.request
from selenium.webdriver.common.by import By


root=tk.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
name_var=tk.StringVar()
passw_var=tk.StringVar()


#login info
username = 'edted24@gmail.com'
password = 'catchbass'

#Login to facbook
url = 'https://www.facebook.com' 
driver = webdriver.Firefox() 
driver.get(url) 
time.sleep(2) 
email = driver.find_element_by_name("email") 
pswrd = driver.find_element_by_name("pass") 
email.send_keys(username)
time.sleep(1) 
pswrd.send_keys(password) 
time.sleep(2) 
email.submit() 
time.sleep(5) 
driver.get('https://mbasic.facebook.com') 
time.sleep(3) 



#intput query
queryterm = 'bass'
searchbar = driver.find_element_by_name("query") 
searchbar.send_keys(queryterm)
searchbar.submit() 
#navigate to photos
time.sleep(2) 
driver.find_element_by_xpath('//a[contains(text(),"More")]').click()
time.sleep(2) 
driver.find_element_by_xpath('//a[contains(text(),"Photos")]').click()

#go through photos and store url of full images to array
xpaths = ['//div[2]/div/div/div/div/div/a/img','//div[2]/a/img','//div[3]/a/img','//div[4]/a/img','//div[5]/a/img','//div[6]/a/img','//div[7]/a/img','//div[8]/a/img','//div[9]/a/img','//div[10]/a/img','//div[11]/a/img','//div[12]/a/img','//div[13]/a/img']
urls = []
pages = 2
for y in range(pages):
    for x in range(13):
        driver.find_element_by_xpath(xpaths[x]).click()

        link = driver.find_element_by_xpath('//a[contains(text(),"View Full Size")]')
        
        url = link.get_attribute("href")

        urls.append(url)
        driver.back()
        
    driver.find_element_by_xpath('//span[contains(.,"See More Results")]').click()


#output info
print(urls)
print("Query Term:" + queryterm)
print("Pages: " + pages)



#jimboonlakelanier 