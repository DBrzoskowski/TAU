import os
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('[GECKO DRIVER] CDA')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

if sys.platform.startswith('win'):
    path = f"{os.path.abspath(os.getcwd())}\\geckodriver.exe"
else:
    path = f"{os.path.abspath(os.getcwd())}/geckodriver"

browser = webdriver.Firefox(service=Service(path))

logger.info('Przechodzę na stronę cda.pl')

browser.set_window_size(1920, 1080)  # Full HD because  x-kom support responsiveness

browser.get('https://www.cda.pl/')
sleep(2)

temp = browser.find_element(By.XPATH, '//*[@id="key"]')
temp.send_keys('niezwykle trudna nazwa do wyszukiwania')
logger.info('Szukanie frazy `niezwykle trudna nazwa do wyszukiwania` na portalu cda.pl')

button = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div[2]/form/button')
button.click()
sleep(1)

error = browser.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[3]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/p')
assert error.text == 'Niestety, nic nie znaleziono. Spróbuj poszerzyć kryteria lub zmienić słowa kluczowe.'
logger.info('Rezultat po braku znalezienia wybranego elementu na cda.pl')

logger.info('Przejście na strone rejestracji')
register = browser.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]/div[3]/ul/li[1]/div/a/span')
register.click()
sleep(1)

logger.info('Uzupełnienie loginu i hasła')
login = browser.find_element(By.XPATH, '//*[@id="email"]')
login.send_keys('PrzykladowyLogin')
password = browser.find_element(By.XPATH, '//*[@id="pass"]')
password.send_keys('PrzykladoweHaslo')

button = browser.find_element(By.XPATH, '//*[@id="btnS"]')
button.click()
sleep(1)
error = browser.find_element(By.XPATH, '//*[@id="emailError"]')
assert error.text == 'Adres email wygląda na niepoprawny'
logger.info('Poprawnie znalezione błędu o złym adresie email')
browser.close()
