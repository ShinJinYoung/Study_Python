from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# NOT INSTALL Chromedriver

#2. DOSI Store GNB 메뉴 이동
driver.get("https://hellbound-dosi-store.line-apps-beta.com")
time.sleep(3)

#Explore 이동
driver.find_element(By.XPATH, "//*[@id='__next']/main/div/div[1]/header/div/div[2]/span/ul/a[2]/span").click()
time.sleep(1)

#Marketplace
driver.find_element(By.XPATH, "//*[@id='__next']/main/div/div[1]/header/div/div[2]/span/ul/a[3]/span").ckick()
time.sleep(1)

#Notice
driver.find_element(By.XPATH, "//*[@id='__next']/main/div/div[1]/header/div/div[2]/span/ul/a[4]/span").click()
time.sleep(1)

#Discord
driver.find_element(By.XPATH, "//*[@id='__next']/main/div/div[1]/header/div/div[3]/ul/a[1]/div/div/svg/path").click()
time.sleep(1)

#Twitter
driver.find_element(By.XPATH, "//*[@id='__next']/main/div/div[1]/header/div/div[3]/ul/a[2]/div/div/svg/path").click()
time.sleep(1)

#DOSI Wallet
driver.find_element(By.XPATH, "//*[@id='__next']/main/div/div[1]/header/div/div[3]/ul/div[1]/div/svg").click()
time.sleep(1)