import pandas as pd
from selenium import webdriver
 
# Here Chrome  will be used
#driver = webdriver.Chrome("C:/Users/valwur0b/chromedriver/chromedriver.exe")
 #implicit wait
#driver.implicitly_wait(2)
#maximize browser
#driver.maximize_window()
#launch URL
#driver.get("https://gwe-assetmanager.eu1.mindsphere.io/entity/681227ed3edd4739b9fc17c6bda40b60/details?selected=9bb0331435044d38b6914da56c7cc3c9")
#identify element
#login =driver.find_element("id","username")


data = pd.read_excel (r"C:/Users/valwur0b/Desktop/Intralogistics/scraper/kanale.xlsx", sheet_name='PDM_OWNER_AD_Z2L3VKK')

i=1
while i<6:
    print(data.iloc[i,0])
    i+=1
#test = data.iloc[0, 1]
#print(test)