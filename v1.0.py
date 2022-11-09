from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import json

browser = webdriver.Firefox()
browser.get('http://brati-mes/monitor/')
time.sleep(3)
username = browser.find_element(By.ID, 'UserName')
password = browser.find_element(By.ID, 'Password')
username.send_keys("el.silva")
password.send_keys("Peguform@098.")
login_attempt = browser.find_element(By.ID, 'entrar').click()
time.sleep(2)

while True:
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    errors = soup.find("h3", {"id": "countFilaPendentes"})
    errors = errors.string
    print(errors)
    browser.refresh()
    time.sleep(3)