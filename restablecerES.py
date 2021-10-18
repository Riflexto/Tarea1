from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome("D:\chromedriver.exe")
web.maximize_window()
web.get("https://www.mentatiendas.es/recuperacion-contrasena")
web.find_element_by_name("email").send_keys("prueba@mail.cl")
web.find_element_by_name("submit").click()
print("finalizado!")
