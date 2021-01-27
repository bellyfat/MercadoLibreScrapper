from time import sleep
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
browser = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
browser.get('https://autos.mercadolibre.com.uy')
sleep(8)
count=0
for ol in range(1,17):
     for li in range(1,4):
      parseol=str(ol)
      parseli=str(li)
      url_img=('https://http2.mlstatic.com/D_NQ_NP_839600-MLU44669200907_012021-W.webp')
      #url_img=browser.find_element_by_xpath('//*[@id="root-app"]/div/div/section/ol['+parseol+']/li['+parseli+']/div/div/div[1]/a/div/div/div/div/div[1]/img').get_attribute('src')
      def foto(name_img):
       name_img=name_img
       img=requests.get(url_img).content
       with open(name_img,'wb') as handler:
        handler.write(img)
       sleep(5) 
      count=count+1
      strcount=str(count)
      name_img=strcount+".jpg"
      foto(name_img)

browser.quit()
