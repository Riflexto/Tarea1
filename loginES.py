from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome("D:\chromedriver.exe")
web.maximize_window()
web.get("https://www.mentatiendas.es/inicio-sesion?back=my-account")
web.find_element_by_name("email").send_keys("prueba@mail.cl")
web.find_element_by_name("password").send_keys("Contraseña123")
web.find_element_by_id("submit-login").click()
'''
for a in range(100):
	web.find_element_by_name("password").clear()
	web.find_element_by_name("password").send_keys(str(10000+a))
	web.find_element_by_id("submit-login").click()
'''
print("finalizado!")
