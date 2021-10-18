from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome("D:\chromedriver.exe")
web.maximize_window()
web.get("https://www.mentatiendas.es/inicio-sesion?create_account=1")
web.find_element_by_name("firstname").send_keys("Nombre")
web.find_element_by_name("lastname").send_keys("Apellido")
web.find_element_by_name("email").send_keys("prueba@mail.cl")
web.find_element_by_name("password").send_keys("Contraseña123")
web.find_element_by_name("psgdpr").click()
web.find_element_by_xpath("//*[@id='customer-form']/footer/button").click()
print("finalizado!")
