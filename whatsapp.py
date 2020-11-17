from selenium import webdriver
import requests 
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys #for keyboard keys pressing like for next line = shift+enter
import time

PATH="C:\\Users\\om\\Downloads\\chromedriver_win32\\chromedriver.exe" #path of chrome webdriver
driver=webdriver.Chrome(PATH)

time.sleep(2)

url="https://web.whatsapp.com/"
driver.get(url)

input("WAIT TILL SCAN QR CODE OF WHATSAPP COMPLETE THEN PRESS ENTER!")

input("NOW OPEN A WHATSAPP CHAT AND PRESS ENTER")
#if you want to automatically open a particular chat, then uncomment below two lines and change the title to the chat of your!
#group=driver.find_element_by_css_selector('span[title="Bot test"]')
#group.click()

def refresh():
    time.sleep(1)

    #total chats in current chat
    chats=driver.find_elements_by_class_name('eRacY')

    #get last message in total chat
    msg=chats[-1].text
    print("Message is:"+msg)

    if msg[0:8]=='\weather': #weather query asked!
        place=msg[9:]
        print("QUERY FOUND !\nPlace to be search is "+place)

        #web scraping of weather from google result:---
        url='https://www.google.com/search?q=weather'+place
        response=requests.get(url)

        soup=bs(response.content,"lxml")

        xpath='/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]' #path of the typing box of whatsapp chat 
        msgbox=driver.find_element_by_xpath(xpath) 
        try:
            temp=soup.find("div",class_='BNeawe iBp4i AP7Wnd').text #temperature
            more=soup.find('div',class_='BNeawe tAd8D AP7Wnd').text #more info
            
            i=more.find('\n')
            cond=more[i+1:] #fog,clear,rain etc
            
            msgbox.send_keys("Place: "+place)
            msgbox.send_keys(Keys.SHIFT+Keys.ENTER)
            
            msgbox.send_keys("Temperature: "+temp)
            msgbox.send_keys(Keys.SHIFT+Keys.ENTER)
            
            msgbox.send_keys("Condition: "+cond)
            msgbox.send_keys(Keys.ENTER)
        except:
            print('\nERROR ====!!!!\n')
            msgbox.send_keys(place+' is not found!')
            msgbox.send_keys(Keys.ENTER)

time.sleep(4)
while True:
    print("-----SCANNING MESSAGES!!!-----")
    refresh()
    time.sleep(3)