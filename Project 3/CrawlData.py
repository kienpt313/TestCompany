from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException
import pandas as pd
import numpy as np
chrome_option=Options()
browser = webdriver.Chrome(chrome_options=chrome_option,executable_path="chromedriver.exe")
browser.get("https://nhadat.cafeland.vn/nha-dat-ban-tai-ha-noi/")
# print(browser.title)
# browser.quit()
datacrawl=[]
trang=1
while True:
    try:
        print("Trang so: "+str(trang))
        trang=trang+1
        elems=browser.find_elements(By.CSS_SELECTOR,".reales-title [href]")
        title =[elem.text for elem in elems]
        links= [elem.get_attribute('href') for elem in elems]
        # print(links)
        for link in links:
            browser.get(link)
            title=browser.title
            TimeUpdate=browser.find_elements(By.CSS_SELECTOR,".reales-location .col-right .infor i")
            TGCN =[elem.text for elem in TimeUpdate]
            print(TGCN[0])
            Location=browser.find_elements(By.CSS_SELECTOR,".reales-location .col-left .infor div:nth-of-type(2)")
            Vitri =[elem.text for elem in Location]
            print(Vitri)
            Money=browser.find_elements(By.CSS_SELECTOR,".reals-info-group .content .col-item:nth-of-type(1) .infor-note")
            Tien =[elem.text for elem in Money]
            print(Tien[1])
            Square=browser.find_elements(By.CSS_SELECTOR,".reals-info-group .content .col-item:nth-of-type(2) .infor-data")
            DTich =[elem.text for elem in Square]
            
            KienTruc=browser.find_elements(By.CSS_SELECTOR,".reals-architecture .value-item")
            KTTI =[elem.text for elem in KienTruc]
            
            description=browser.find_elements(By.CSS_SELECTOR,".reals-description div:nth-of-type(2)")
            description1 =[elem.text for elem in description]
            
            dataGround= {        'Title':            title,
                                'Thời gian':        TGCN[0],
                                'Vị Trí':           Vitri[0],
                                'Giá':              Tien[1],
                                'Diện tích':        DTich[0],
                                'Loại':             KTTI[0],
                                'Hướng':            KTTI[1],
                                'tầng':             KTTI[2],
                                'Tolet':            KTTI[3],
                                'Đường':            KTTI[4],
                                'Phòng khách':      KTTI[5],
                                'Phòng ngủ':        KTTI[6],
                                'Pháp lý':          KTTI[7],
                                'Nội dung':         description1[0],
                                }
            datacrawl.append(dataGround)
        browser.get("https://nhadat.cafeland.vn/nha-dat-ban-tai-ha-noi/page-"+str(trang)+"/")
        if trang==200:
            break
    except ElementNotInteractableException:
        print("Element Not Interactable Exception")
        break
df= pd.DataFrame(datacrawl)
df.to_csv('NhaDat.csv')

        #dong trinh duyet
sleep(3)
browser.close()