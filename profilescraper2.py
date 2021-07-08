
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from tkinter import *
from functools import partial
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def execute(username,password,url):

    #Login to facbook
    start = 'https://www.facebook.com' 

    driver = webdriver.Firefox(executable_path=resource_path('./driver/geckodriver.exe'))
    
    driver.get(start) 
    time.sleep(2) 
    email = driver.find_element_by_name("email") 
    pswrd = driver.find_element_by_name("pass") 
    email.send_keys(username.get())
    time.sleep(1) 
    pswrd.send_keys(password.get()) 
    time.sleep(2) 
    email.submit() 
    time.sleep(5) 
    driver.get(url.get()) 
    url
    time.sleep(3) 

    def check_exists_by_text(text):
        if text not in driver.page_source :
            return False
        return True


    driver.find_element_by_xpath('/html/body/div/div/div/div/table/tbody/tr/td/div/a[1]').click()

    urls = []
    while check_exists_by_text("Next"):
        link = driver.find_element_by_xpath('//a[contains(text(),"View Full Size")]')
        url = link.get_attribute("href")
        urls.append(url)
        driver.find_element_by_xpath('//a[contains(.,"Next")]').click()    
        time.sleep(.5) 

        


    #output info
    with open("data"+'.csv','w', newline="") as out:
                csv_out=csv.writer(out)
                csv_out.writerow(['url',' '])
                for row in urls:
                    csv_out.writerow([row," "])


#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Login Form')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

urlLabel = Label(tkWindow,text="mbasic url").grid(row=2, column=0)  
url = StringVar()
urlEntry = Entry(tkWindow, textvariable=url).grid(row=2, column=1)  

execute = partial(execute, username, password, url)


loginButton = Button(tkWindow, text="Login", command=execute).grid(row=4, column=0)  

tkWindow.mainloop()








