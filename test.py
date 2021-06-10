import time
from bs4 import BeautifulSoup
import cloudscraper
from pytz import timezone
start_time = time.time()
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver2 = webdriver.Chrome(ChromeDriverManager().install())
url2 = f'https://www.pedigreequery.com/'
driver2.get(url2)
time.sleep(10)

with open('test.html', 'a', encoding='utf-8') as pedigrees:
    pedigrees.write("<!DOCTYPE html><html lang='en'><body>")
    dam_father = "Horse Chestnut"
    dam = "Aesculus"
    search_box = driver2.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr/td[1]/input').send_keys(dam)
    search_button = driver2.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr/td[6]/input').click()
    if str(driver2.page_source).find('tablesorter') > 0:
        dam_fathers = driver2.find_elements_by_xpath('/html/body/table/tbody/tr[5]/td[1]/blockquote/table/tbody/tr')
        for each in range(1, len(dam_fathers) + 1):
            father = driver2.find_element_by_xpath(f'/html/body/table/tbody/tr[5]/td[1]/blockquote/table/tbody/tr[{each}]/td[5]/a').text
            if father.find(dam_father.upper().replace("'","")) >= 0:
                tem_each = ""
                if each != 1:
                    tem_each = str(each)
                url3 = "https://www.pedigreequery.com/{m}{n}".format(m="+".join(dam.lower().split(" ")), n=tem_each)
                driver2.get(url3)
                time.sleep(1)
                pedigree_table = driver2.find_element_by_class_name('pedigreetable').get_attribute('innerHTML')
                pedigrees.write("<center>" + "<table border='1' cellpadding='0'>" + str(pedigree_table) + "/<table>" + "</center>")
                break
    else:
        pedigree_table = driver2.find_element_by_class_name('pedigreetable').get_attribute('innerHTML')
        pedigrees.write("<center>" + "<table border='1' cellpadding='0'>" + str(pedigree_table) + "/<table>" + "</center>")
    pedigrees.write("</body></html>")
# tablesorter_is = driver2.text.find('tablesorter')
# print(tablesorter_is)