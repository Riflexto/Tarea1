from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome("D:\chromedriver.exe")
web.maximize_window()
web.get("https://www.pizzapizza.cl/tu-cuenta/")
web.find_element_by_name("username").send_keys("riflext@gmail.com")
web.find_element_by_name("password").send_keys("Contraseña1234")
web.find_element_by_name("login").click()
web.get("https://www.pizzapizza.cl/tu-cuenta/edit-account/")
web.find_element_by_id("password_current").send_keys("Contraseña1234")
web.find_element_by_id("password_1").send_keys("Contraseñafuerte123")
web.find_element_by_id("password_2").send_keys("Contraseñafuerte123")
web.find_element_by_name("save_account_details").click()
print("finalizado!")
