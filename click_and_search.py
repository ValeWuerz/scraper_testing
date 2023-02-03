
# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# Here Chrome  will be used
driver = webdriver.Chrome("C:/Users/valwur0b/chromedriver/chromedriver.exe")
 #implicit wait
driver.implicitly_wait(0.5)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://www.google.de/")
#identify element
l =driver.find_element("id","W0wltc")
#perform click
l.click()

inputfield = driver.find_element("xpath", "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
inputfield.send_keys("testing")
search = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]" )
search.click()
""" relation = driver.find_element("xpath","/html/body/div[7]/div/div[4]/div/div[1]/div/div[1]/div/div[1]/span" )
ac= ActionChains(driver)
ac.move_to_element_with_offset(relation, 0, 200).click().perform()
ac.move_to_element_with_offset(relation, 0, 300).click().perform()
ac.move_to_element_with_offset(relation, 0, 400).click().perform() """

#print("Page title is: ")
#print(driver.title)
#close browser
# URL of website
 
