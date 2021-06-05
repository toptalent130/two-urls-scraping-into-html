# start source file
from selenium import webdriver
import time
import argparse
import itertools
import xlsxwriter
import sys, getopt
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.support.select import Select
import time
from bs4 import BeautifulSoup
import re
import pickle
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.keys import Keys
import cloudscraper
from datetime import datetime
from pytz import timezone
from webdriver_manager.chrome import ChromeDriverManager
start_time = time.time()
# scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
# # Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
# text = scraper.get("https://www.pedigreequery.com/terra+aqua").text
# bst = BeautifulSoup(text,'lxml')
# links = bst.findAll('td',{'class':{'f'}})
# for link in links:
#   print(link.get_text().replace('\n',''))

workbook = xlsxwriter.Workbook('hello.xlsx') 
  
worksheet = workbook.add_worksheet() 

chrome_options = Options()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# driver = webdriver.Chrome('C:/py/chrome/chromedriver.exe',options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install())



armenia = timezone('Asia/Yerevan')
month = datetime.now(tz=armenia).month
day = datetime.now(tz=armenia).day
if month < 10:
  month = "0" + str(month)
else:
  month = str(month)
if day < 10:
  day = "0" + str(day)
else:
  day = str(day)
date = month +  day

url = f'https://www.equibase.com/static/entry/PIM{date}21USA-EQB.html'

print(url)
driver.get(url)
horsecount = 1
time.sleep(90)
with open('result.csv','a', encoding='utf-8') as f:
  firstrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr')
  if len(firstrace) != 0:
    while True:
      try:
        firstrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr')
        if len(firstrace) != 0:
          for i in range(len(firstrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass

    while True:
      try:
        secondrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[3]/div[3]/table/tbody/tr')
        if len(secondrace) != 0:
          for i in range(len(secondrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[3]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[3]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass

    while True:
      try:
        thirdrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[5]/div[3]/table/tbody/tr')
        if len(thirdrace) != 0:
          for i in range(len(thirdrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[5]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[5]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass

    while True:
      try:
        fourthrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[7]/div[3]/table/tbody/tr')
        if len(fourthrace) != 0:
          for i in range(len(fourthrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[7]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[7]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass

    while True:
      try:
        fifthrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[9]/div[3]/table/tbody/tr')
        if len(fifthrace) != 0:
          for i in range(len(fifthrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[9]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[9]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass


    while True:
      try:
        sixthrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[11]/div[3]/table/tbody/tr')
        if len(sixthrace) != 0:
          for i in range(len(sixthrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[11]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[11]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass

    while True:
      try:
        seventhrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[13]/div[3]/table/tbody/tr')
        if len(seventhrace) != 0:
          for i in range(len(seventhrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[13]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[13]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass


    while True:
      try:
        eighthrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[15]/div[3]/table/tbody/tr')
        if len(eighthrace) != 0:
          for i in range(len(eighthrace)):
            try:
              horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[15]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
              if horsename1.text != '':
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
              else:
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[15]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                worksheet.write('A{x}'.format(x=horsecount), horsename1.text[:-4])
            except:
              pass
            horsecount = horsecount + 1
          break
        time.sleep(2)
      except:
        pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[0].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[0].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[1].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[1].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[2].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[2].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[3].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[3].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[4].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[4].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[5].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[5].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[6].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[6].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[7].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[7].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[8].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[8].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[9].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[9].innerText='';")
    except:
      pass
    try:
      driver.execute_script("document.getElementsByClassName('contenders')[10].innerText='';")
      driver.execute_script("document.getElementsByClassName('bg-tan')[10].innerText='';")
    except:
      pass
    gencount = 1
    famcount = 1
    fam1 = driver.find_elements_by_tag_name('a')
    try:
      for f in fam1:
        try:
          name = f.get_attribute('data-original-title')
          print("****", name)
          if len(name) > 4:
            scraper = cloudscraper.create_scraper()
            # Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
            text = scraper.get("https://www.pedigreequery.com/{m}".format(m=name.replace('(','').replace(')','').partition("- ")[2].partition(",")[0].replace(' ','+'))).text
            bst = BeautifulSoup(text,'lxml')
            links = bst.findAll('td',{'class':{'f'}})
            for link in links:
              worksheet.write('B{x}'.format(x=gencount), link.get_text())
              gencount = gencount + 1
            famcount = famcount + 1
            gencount = gencount + 1
            worksheet.write('B{x}'.format(x=gencount), '\n\n')
        except:
          pass
    except:
      pass
  else:
    print('********there are no races today********')

workbook.close()
print("--- %s seconds ---" % (time.time() - start_time))
