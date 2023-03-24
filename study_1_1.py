from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# NOT INSTALL Chromedriver

#1. DOSI Wallet 로그인
driver.get("https://dosi-wallet.line-apps-beta.com")
time.sleep(3)

#모두 허용
#driver.find_element(By.CLASS_NAME, "btn").click()
driver.find_element(By.CLASS_NAME, "btn").send_keys(Keys.ENTER)
time.sleep(1)

#로그인
#driver.find_element(By.XPATH, "//*[@id='root']/main/div/button").click()
#time.sleep(1)

#LINE으로 로그인
driver.find_element(By.XPATH, "//*[@id='social-providers']/a[1]").click()
time.sleep(1)

# #Facebook으로 로그인
# driver.find_element(By.XPATH, "//*[@id='social-providers']/a[2]")
# #Google로 로그인
# driver.find_element(By.XPATH, "//*[@id='social-providers']/a[3]")
# #Naver로 로그인
# driver.find_element(By.XPATH, "//*[@id='social-providers']/a[4]")

#이메일
email = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div/form/fieldset/div[1]/input")
email.send_keys("dosi_kr_3@yopmail.com")
time.sleep(1)

#비밀번호
password = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div/form/fieldset/div[2]/input")
password.send_keys("lbd123")
time.sleep(1)

#로그인
driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div/form/fieldset/div[3]/button").click()
time.sleep(1)

#허용
driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div/div/div/form/div/button").click()
time.sleep(1)

#패스코드
driver.find_element(By.XPATH, "//*[@id='root']/main/section/div[2]/button[1]").click() #1
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='root']/main/section/div[2]/button[4]").click() #4
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='root']/main/section/div[2]/button[7]").click() #7
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='root']/main/section/div[2]/button[1]").click() #1
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='root']/main/section/div[2]/button[4]").click() #4
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='root']/main/section/div[2]/button[7]").click() #7
time.sleep(1)