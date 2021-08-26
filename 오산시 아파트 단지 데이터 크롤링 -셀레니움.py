#!/usr/bin/env python
# coding: utf-8

# In[8]:


from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

wd= webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

wd.get('http://land.ohkcr.com/map/apt/')

know='경기도 오산시'

searchbox = wd.find_element_by_css_selector("input#searchText") 
searchbox.send_keys(know)
searchbox.send_keys(Keys.RETURN)
time.sleep(2)

apt_result=[]
result1=[]
result2=[]
result3=[] # 단지종류
result4=[] # 총 세대수
result5=[] # 전용면적1


for i in range(100,999):
    try:
        wd.find_element_by_xpath('//*[@id="apt_1025{}"]'.format(i)).click()
        wd.find_element_by_xpath('//*[@id="articleViewTab"]/li[3]/a').click()
        text1=wd.find_element_by_xpath(' //*[@id="articleViewHeader"]/h3').text
        text2=wd.find_element_by_xpath('//*[@id="aptInfoJs"]/table/tbody/tr[3]/td[1]').text
        text3=wd.find_element_by_xpath('//*[@id="articleViewHeader"]/p[2]').text  
        text4=wd.find_element_by_xpath('//*[@id="aptInfoJs"]/table/tbody/tr[1]/td[1]').text # 단지종류
        text5=wd.find_element_by_xpath('//*[@id="aptInfoJs"]/table/tbody/tr[1]/td[2]').text #총 세대수
    
        text6=wd.find_element_by_xpath('//*[@id="aptInfoJs"]/table/tbody/tr[2]/td[1]').text  #전용면적1
        
        apt_result.append(text1)
        result1.append(text2)
        result2.append(text3)
        result3.append(text4)
        result4.append(text5)
        result5.append(text6)
        
        
    except:
        print('no')
df= pd.DataFrame(
                {'name' : apt_result,
                 '주차대수' : result1,
                 '주소': result2,
                 '단지종류': result3,
                 '총 세대수' : result4,
                 '전용면적' : result5
                }
                )
df.to_csv('C:/Users/신은주/Desktop/오산시 데이터/오산시_단지 이름,주차대수,주소지.csv', index = False, encoding='utf-8-sig')


# In[22]:


df.head()

