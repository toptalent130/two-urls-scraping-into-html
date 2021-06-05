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
start_time = time.time()
from webdriver_manager.chrome import ChromeDriverManager

# workbook = xlsxwriter.Workbook('result.xlsx') 
# worksheet = workbook.add_worksheet() 
chrome_options = Options()
chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

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
driver.get(url)

time.sleep(90)
raceindex = 1
trigger = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr')

with open('pedigrees.html','a', encoding='utf-8') as pedigrees:
    pedigrees.write("<!DOCTYPE html><html lang='en'><body>")
    if len(trigger) != 0:
        firstrace = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr')
        pedigrees.write("<div style='background-color:green'><h2 style='color:white'> Rase" + str(raceindex) + " horses </h2></div>")
        print("**************scraping{}*****************".format(raceindex))
        for i in range(len(firstrace)):
            horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
            if horsename1.text == '':
                horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))               
            time.sleep(1)
            fam1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[3]/b/a'.format(i=i+1))
            try:
                name = fam1.get_attribute('data-original-title')
                dam = name.split("-")[1].split(",")[0][1:]
                pedigrees.write("<center><h3 style='color:red'>" + dam +"</h3><h5>" + horsename1.text[:-4] + "</h5></center>")
                print("horse name:  ", horsename1.text[:-4] , "mother:   ", dam)
                scraper = cloudscraper.create_scraper()
                text = scraper.get("https://www.pedigreequery.com/{m}".format(m="+".join(name.split("-")[1].split(",")[0][1:].split(" ")))).text
                bst = BeautifulSoup(text,'html.parser')
                generations = bst.find_all('table', {"class": "pedigreetable"})
                pedigrees.write("<center>" + str(generations[0]) + "</center>")
            except:
                pass
        time.sleep(2)
        raceindex = raceindex + 1
        while True:
            race = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr'.format(j=raceindex*2-1))
            if len(race) != 0:
                pedigrees.write("<div style='background-color:green'><h2 style='color:white'> Rase" + str(raceindex) + " horses </h2></div>")
                for i in range(len(race)):
                    trigger1 = driver.find_elements_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td'.format(j=raceindex*2-1,i=i+1))
                    if len(trigger1) > 3:
                        horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td[3]'.format(j=raceindex*2-1,i=i+1))
                        if horsename1.text == '':
                            horsename1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td[2]'.format(j=raceindex*2-1,i=i+1))               
                        time.sleep(1)
                        fam1 = driver.find_element_by_xpath('/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td[3]/b/a'.format(j=raceindex*2-1,i=i+1))
                        try:
                            name = fam1.get_attribute('data-original-title')
                            dam = name.split("-")[1].split(",")[0][1:]
                            pedigrees.write("<center><h3 style='color:red'>" + dam +"</h3><h5>" + horsename1.text[:-4] + "</h5></center>")
                            print("horse name:  ", horsename1.text[:-4] , "mother:   ", dam)
                            scraper = cloudscraper.create_scraper()
                            text = scraper.get("https://www.pedigreequery.com/{m}".format(m="+".join(name.split("-")[1].split(",")[0][1:].split(" ")))).text
                            bst = BeautifulSoup(text,'html.parser')
                            generations = bst.find_all('table', {"class": "pedigreetable"})
                            pedigrees.write("<center>" + str(generations[0]) + "</center>")
                        except:
                            pass
            else:
                break
            time.sleep(2)
            raceindex = raceindex + 1
    else:
        print('********there are no races today********')
    pedigrees.write("</body></html>")
    pedigrees.close()