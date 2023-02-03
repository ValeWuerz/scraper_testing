# importing webdriver from selenium
from selenium import webdriver
 
# Here Chrome  will be used
driver = webdriver.Chrome("C:/Users/valwur0b/chromedriver/chromedriver.exe")
 #implicit wait
driver.implicitly_wait(2)
#maximize browser
driver.maximize_window()
#launch URL
driver.get("https://digicampus.uni-augsburg.de/dispatch.php/start?sso=webauth&cancel_login=1&again=yes")
#identify element
login =driver.find_element("id","username")
password =driver.find_element("id","password")
submit =driver.find_element("xpath","/html/body/div/div/div/div/form/div[3]/button")
login.send_keys("wuerzval")
password.send_keys("D56jIkAP")
submit.click()