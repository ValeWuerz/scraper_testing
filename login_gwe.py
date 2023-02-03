# importing webdriver from selenium
from cmath import log
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
data = pd.read_excel (r"C:/Users/valwur0b/Desktop/Intralogistics/scraper/kanale.xlsx", sheet_name='PDM_OWNER_AD_Z2L3VKK')

# Here Chrome  will be used
driver = webdriver.Chrome("C:/Users/valwur0b/chromedriver/chromedriver.exe")
 #implicit wait
driver.implicitly_wait(2)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://gwe-assetmanager.eu1.mindsphere.io/entity/764b6e51ca5c40ebb5b1b49958bb0ea9/details")

#login to gwe
login =driver.find_element("id","username")
password =driver.find_element("id","password")
submit =driver.find_element("id","submit")
login.send_keys("valentin.wuerz@siemens.com")
password.send_keys("traV_Fladuz!2")
submit.click()
#elect asset
divnum=2
while divnum<200:
    driver.implicitly_wait(30)
    time.sleep(2)

    channel_button = driver.find_element("xpath", f'/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[2]/sie-app-layout-regions-leading-region/mdsp-app-layout-leading-region/mdsp-asset-navigation/div/nav/mdsp-navigation-list/div/div/div/ul/virtual-scroller/div[2]/div[{divnum}]')
    print(channel_button)
      
    channel_button.click()
    time.sleep(1)
    #driver.execute_script("document.getElementById('mdspCore-navbar__items').scrollBy(0, 46);")
    time.sleep(1)
    channelnamepath = driver.find_element("xpath", f'/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[2]/sie-app-layout-regions-leading-region/mdsp-app-layout-leading-region/mdsp-asset-navigation/div/nav/mdsp-navigation-list/div/div/div/ul/virtual-scroller/div[2]/div[{divnum}]/mdsp-navigation-list-item/li/div/mdsp-navigation-list-item-content/div/h4')
    channelname = channelnamepath.get_attribute('innerHTML')
    print(channelname)
    select_but=driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-detail-container/mdsp-asset-detail/section/header/mdsp-asset-tool-bar/mdsp-tool-bar/div/div[2]/div/div/mdsp-actions-menu/div/div[1]/mdsp-actions-menu-item[1]/button")
    time.sleep(2)
    select_but.click()
    
    inputfield_Name = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[2]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_Name.clear()
    inputfield_Name.send_keys(channelname)
    inputfield_lenght = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[1]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_type = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[3]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_loc = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[4]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_minfill = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[5]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_prodline = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[6]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_reptime = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[7]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_sens1 = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[8]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_sens2 = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[9]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_sens3 = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[10]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")
    inputfield_sens4 = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[2]/p-fieldset/fieldset/div/div/div/mdsp-variable-list-table-container/section/mdsp-variable-list-table/p-table/div/div/table/tbody/tr[11]/td[5]/mdsp-variable-input/mdsp-data-table-input-wrapper/div/input")

    i=1
    while i<423:
        name = data.iloc[i,0]

        if(name == channelname):
            c_type=data.iloc[i,1]
            c_length=data.iloc[i,2]
            c_location=data.iloc[i,3]
            c_minfill=data.iloc[i,4]
            c_prodline=data.iloc[i,5]
            c_reptime=data.iloc[i,6]
            c_sens1=data.iloc[i,7]
            c_sens2=data.iloc[i,8]
            c_sens3=data.iloc[i,9]
            c_sens4=data.iloc[i,10]
            print(c_type)
            print(c_length)
            print(c_location)
            print(c_minfill)
            break
        i+=1
    inputfield_type.clear()
    inputfield_type.send_keys(c_type)
    inputfield_loc.clear()
    inputfield_loc.send_keys(c_location)
    inputfield_minfill.clear()
    inputfield_minfill.send_keys(str(c_minfill))
    inputfield_prodline.clear()
    inputfield_prodline.send_keys(c_prodline)
    inputfield_reptime.clear()
    inputfield_reptime.send_keys(str(c_reptime))
    inputfield_lenght.clear()
    inputfield_lenght.send_keys(str(c_length))
    inputfield_sens1.clear()
    inputfield_sens1.send_keys(c_sens1)
    inputfield_sens2.clear()
    inputfield_sens2.send_keys(c_sens2)
    inputfield_sens3.clear()
    inputfield_sens3.send_keys(c_sens3)
    inputfield_sens4.clear()
    inputfield_sens4.send_keys(c_sens4)

    submit = driver.find_element("xpath", "/html/body/div/mdsp-root/mdsp-app-layout/sie-app-layout/div/sie-app-layout-regions/div/section[3]/sie-app-layout-regions-main-region/mdsp-asset/mdsp-asset-edit/mdsp-asset-form-container/mdsp-content-section/div/div[5]/button[1]")
    submit.click()
    print(channelname + " submitted")
    time.sleep(2)

    print("reloaded")
    
    divnum+=1

