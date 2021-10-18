from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

web = webdriver.Chrome("D:\chromedriver.exe")
web.maximize_window()
web.get("https://www.pizzapizza.cl/tu-cuenta/")
web.find_element_by_id("reg_username").send_keys("UsuarioA")
web.find_element_by_id("reg_email").send_keys("prueba@mail.cl")
web.find_element_by_id("reg_password").send_keys("Contraseña123")
web.find_element_by_name("register").click()
print("finalizado!")
