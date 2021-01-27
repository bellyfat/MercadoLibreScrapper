from time import sleep
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
datos=[]

def Scrapping(url):
    browser.get(url)
    sleep(8)
    for ol in range(1,17):
     for li in range(1,4):
         parseol=str(ol)
         parseli=str(li)
         url=browser.find_element_by_xpath('//*[@id="root-app"]/div/div/section//ol['+parseol+']/li['+parseli+']/div/div/div[1]/a').get_attribute('href')
         title=browser.find_elements_by_xpath('//*[@id="root-app"]/div/div/section/ol['+parseol+']/li['+parseli+']/div/div/a/div/div[3]/h2')[0].text
         precio=browser.find_elements_by_xpath('//*[@id="root-app"]/div/div/section/ol['+parseol+']/li['+parseli+']/div/div/a/div/div[1]/div/div/span/span[2]')[0].text
         km=browser.find_elements_by_xpath('//*[@id="root-app"]/div/div/section/ol['+parseol+']/li['+parseli+']/div/div/a/div/div[2]/ul/li[2]')[0].text
         año=browser.find_elements_by_xpath('//*[@id="root-app"]/div/div/section/ol['+parseol+']/li['+parseli+']/div/div/a/div/div[2]/ul/li[1]')[0].text
         ubicacion=browser.find_elements_by_xpath('//*[@id="root-app"]/div/div/section/ol['+parseol+']/li['+parseli+']/div/div/a/div/div[4]/span')[0].text
         cars_data={'Auto':title,'precio':precio,'km':km,'año':año,'ubicacion':ubicacion,'url':url}
        
         def savedata(datos):
            string="{},{},{},{},{},{}".format(
                cars_data['Auto'],
                cars_data['precio'],
                cars_data['km'],
                cars_data['año'],
                cars_data['ubicacion'],
                cars_data['url'],
                )
            save(string,'autos.csv')    
         price=precio.replace('.','')
         priceint=int(price)
         if(priceint<5000):
          savedata(datos)
    return datos
num=1

def save(text,csv):
    print(text)
    with open(csv,'a') as fd:
        fd.write(text+'\n')



while True:
 parseo=str(num)
 url='https://autos.mercadolibre.com.uy/_Desde_'+parseo
 Scrapping(url)
 num=num+48
 sleep(10)

browser.quit()