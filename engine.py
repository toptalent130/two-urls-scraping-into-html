
import time
from bs4 import BeautifulSoup
import cloudscraper
from pytz import timezone
start_time = time.time()
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

def filterName(name):
    tem_dam = name.split(" ")
    array_dam = []
    for ele in range(len(tem_dam)):
        if tem_dam[ele].find("(") < 0 or tem_dam[ele].find(")") < 0:
            array_dam.append(tem_dam[ele])
    return " ".join(array_dam)
def GetDataFrom(driver, driver2, date, type, track):
    # chrome_options = Options()
    # chrome_options.add_argument(
    #     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
    # chrome_options.add_experimental_option(
    #     "excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', False)
    # chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    url1 = f'https://www.equibase.com/static/entry/{track}{date}21USA-EQB.html'
    driver.get(url1)

    time.sleep(60)

    url2 = f'https://www.pedigreequery.com/'
    driver2.get(url2)

    raceindex = 1
    trigger = driver.find_elements_by_xpath(
        '/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr')

    with open('pedigrees_{}_by {}.html'.format(date, type), 'a', encoding='utf-8') as pedigrees:
        pedigrees.write("<!DOCTYPE html><html lang='en'><body>")
        if len(trigger) != 0:
            firstrace = driver.find_elements_by_xpath(
                '/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr')
            pedigrees.write("<div style='background-color:green'><h2 style='color:white'> Rase" +
                            str(raceindex) + " horses </h2></div>")
            print("**************scraping{}*****************".format(raceindex))
            for i in range(len(firstrace)):
                horsename1 = driver.find_element_by_xpath(
                    '/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[3]'.format(i=i+1))
                if horsename1.text == '':
                    horsename1 = driver.find_element_by_xpath(
                        '/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[2]'.format(i=i+1))
                time.sleep(1)
                fam1 = driver.find_element_by_xpath(
                    '/html/body/section[4]/div/div[1]/div/div/div[1]/div[3]/table/tbody/tr[{i}]/td[3]/b/a'.format(i=i+1))
                try:
                    name = fam1.get_attribute('data-original-title')
                    horsename = filterName(horsename1.text)
                    dam = ""
                    dam_father = ""
                    if type == "dam":
                        dam = filterName(name.split("-")[1].split(",")[0][1:])
                        dam_father = filterName(name.split("-")[1].split(",")[1][4:-1])
                        pedigrees.write("<center><h3 style='color:red'>" + dam +
                                    "</h3><h5>of: " + horsename + "</h5></center>")
                        print("--->horse name:  ",
                            horsename, "---->mother:   ", dam)
                    elif type == "horse":
                        dam = horsename
                        dam_father = filterName(name.split("-")[0][2:-1])
                        pedigrees.write("<center><h3 style='color:red'>" + horsename +
                                    "</h3></center>")
                        print("--->horse name:  ",
                            horsename, "---->father:   ", dam_father)

                    driver2.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr/td[1]/input').send_keys(dam)
                    driver2.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr/td[6]/input').click()
                    time.sleep(2)
                    if str(driver2.page_source).find('tablesorter') > 0:
                        dam_fathers = driver2.find_elements_by_xpath('/html/body/table/tbody/tr[5]/td[1]/blockquote/table/tbody/tr')
                        for each in range(1, len(dam_fathers) + 1):
                            father = driver2.find_element_by_xpath(f'/html/body/table/tbody/tr[5]/td[1]/blockquote/table/tbody/tr[{each}]/td[5]/a').text
                            print(">>>>father:",father,">>>>dam_father:",dam_father.upper().replace("'",""))
                            if father.find(dam_father.upper().replace("'","")) >= 0:
                                tem_each = ""
                                if each != 1:
                                    tem_each = str(each)
                                url3 = "https://www.pedigreequery.com/{m}{n}".format(m="+".join(dam.lower().split(" ")), n=tem_each)
                                driver2.get(url3)
                                time.sleep(2)
                                pedigree_table = driver2.find_element_by_class_name('pedigreetable').get_attribute('innerHTML')
                                pedigrees.write("<center>" + "<table border='1' cellpadding='0'>" + str(pedigree_table) + "/<table>" + "</center>")
                                break
                    else:
                        pedigree_table = driver2.find_element_by_class_name('pedigreetable').get_attribute('innerHTML')
                        pedigrees.write("<center>" + "<table border='1' cellpadding='0'>" + str(pedigree_table) + "/<table>" + "</center>")
                    
                except:
                    pass
            time.sleep(2)
            raceindex = raceindex + 1
            while True:
                race = driver.find_elements_by_xpath(
                    '/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr'.format(j=raceindex*2-1))
                if len(race) != 0:
                    pedigrees.write("<div style='background-color:green'><h2 style='color:white'> Rase" +
                                    str(raceindex) + " horses </h2></div>")
                    print("**************scraping{}*****************".format(raceindex))
                    for i in range(len(race)):
                        trigger1 = driver.find_elements_by_xpath(
                            '/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td'.format(j=raceindex*2-1, i=i+1))
                        if len(trigger1) > 6:
                            horsename1 = driver.find_element_by_xpath(
                                '/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td[3]'.format(j=raceindex*2-1, i=i+1))
                            if horsename1.text == '':
                                horsename1 = driver.find_element_by_xpath(
                                    '/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td[2]'.format(j=raceindex*2-1, i=i+1))
                            time.sleep(1)
                            fam1 = driver.find_element_by_xpath(
                                '/html/body/section[4]/div/div[1]/div/div/div[2]/div[{j}]/div[3]/table/tbody/tr[{i}]/td[3]/b/a'.format(j=raceindex*2-1, i=i+1))
                            try:
                                name = fam1.get_attribute('data-original-title')
                                print("")
                                horsename = filterName(horsename1.text)
                                dam = ""
                                dam_father = ""
                                if type == "dam":
                                    dam = filterName(name.split("-")[1].split(",")[0][1:])
                                    dam_father = filterName(name.split("-")[1].split(",")[1][4:-1])
                                    pedigrees.write("<center><h3 style='color:red'>" + dam + "</h3><h5>of: " + horsename + "</h5></center>")
                                    print("--->horse name:  ", horsename, "---->mother:   ", dam)
                                elif type == "horse":
                                    dam = horsename
                                    dam_father = filterName(name.split("-")[0][2:-1])
                                    pedigrees.write("<center><h3 style='color:red'>" + horsename + "</h3></center>")
                                    print("--->horse name:  ", horsename, "---->father:   ", dam_father)


                                driver2.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr/td[1]/input').send_keys(dam)
                                driver2.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr/td[6]/input').click()
                                if str(driver2.page_source).find('tablesorter') >= 0:
                                    dam_fathers = driver2.find_elements_by_xpath('/html/body/table/tbody/tr[5]/td[1]/blockquote/table/tbody/tr')
                                    for each in range(1, len(dam_fathers) + 1):
                                        father = driver2.find_element_by_xpath(f'/html/body/table/tbody/tr[5]/td[1]/blockquote/table/tbody/tr[{each}]/td[5]/a').text
                                        if father.find(dam_father.upper().replace("'","")) >= 0:
                                            tem_each = ""
                                            if each != 1:
                                                tem_each = str(each)
                                            url3 = "https://www.pedigreequery.com/{m}{n}".format(m="+".join(dam.lower().split(" ")), n=tem_each)
                                            driver2.get(url3)
                                            time.sleep(2)
                                            pedigree_table = driver2.find_element_by_class_name('pedigreetable').get_attribute('innerHTML')
                                            pedigrees.write("<center>" + "<table border='1' cellpadding='0'>" + str(pedigree_table) + "/<table>" + "</center>")
                                            break
                                else:
                                    pedigree_table = driver2.find_element_by_class_name('pedigreetable').get_attribute('innerHTML')
                                    pedigrees.write("<center>" + "<table border='1' cellpadding='0'>" + str(pedigree_table) + "/<table>" + "</center>")
                                
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


