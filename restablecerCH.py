from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome("D:\chromedriver.exe")
web.maximize_window()
web.get("https://www.pizzapizza.cl/admin-2x1/?action=lostpassword")
web.find_element_by_name("user_login").send_keys("riflext@gmail.com")
web.find_element_by_name("wp-submit").click()
print("finalizado!")
