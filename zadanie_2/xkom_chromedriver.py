import os
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('[CHROME DRIVER] X-KOM')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

if sys.platform.startswith('win'):
    path = f"{os.path.abspath(os.getcwd())}\\chromedriver.exe"
else:
    path = f"{os.path.abspath(os.getcwd())}/chromedriver"

browser = webdriver.Chrome(service=Service(path))

logger.info('Przechodzę na stronę x-kom.pl')

browser.set_window_size(1920, 1080)  # Full HD because  x-kom support responsiveness

browser.get('https://www.x-kom.pl/')
sleep(2)

temp = browser.find_element(By.XPATH, '//*[@id="app"]/div[1]/header/div[1]/div[4]/div/div[2]/div/div/a')
temp.click()
logger.info('Przechodze na stronę logowania')

sleep(1)
logger.info('Uzupełniam dane logowania')
login = browser.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div/form/div[1]/label/input')
login.send_keys('admin')

button = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/form/button')
button.click()
sleep(1)

logger.info('Pobieram informacje o błędzie')
error = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[2]/span')

assert error.text == 'Wpisz hasło. Pole nie może być puste'

logger.info('Uzupełnianie hasła po informacji o braku jego podania')
password = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/form/div[2]/div/label/input')
password.send_keys('admin')
sleep(1)

logger.info('Poprawnie znalezione błędu dla braku podania hasła do loginu')


button = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/form/button')
button.click()
sleep(1)

logger.info('Pobieram informacje o błędzie')
error = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div[1]/div/form/span')
assert error.text == 'Sprawdź, czy adres e-mail i hasło są poprawne'

logger.info('Poprawnie znalezione błędu o złym adresie email lub haśle')
browser.close()
