from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# NOT INSTALL Chromedriver

driver.get("https://dosi-wallet.line-apps-beta.com")
time.sleep(3)

#모두 허용
driver.find_element(By.CLASS_NAME, "btnbtn").click()
#driver.find_element(By.CSS_SELECTOR, "#root > div > div > div > button:nth-child(2)").click()
#driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/button[2]").click()

#로그인
#driver.find_element(By.CLASS_NAME, "btn full").click()
driver.find_element(By.XPATH, "//*[@id='root']/main/div/button").click()

#LINE으로 로그인
#driver.find_element(By.CLASS_NAME, "Login_social__1KGJg").click()
driver.find_element(By.XPATH, "//*[@id='social-providers']/a[1]").click()

#email = driver.find_element(By.NAME, "tid") #이메일
email = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div/form/fieldset/div[1]/input") #이메일
email.send_keys("dosi_kr_3@yopmail.com")
#password = driver.find_element(By.NAME, "tpasswd") #비밀번호
password = driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div/form/fieldset/div[2]/input") #비밀번호
password.send_keys("lbd123")
#driver.find_element(By.CLASS_NAME, "MdBtn01 ExDisabled").click() #로그인
driver.find_element(By.XPATH, "//*[@id='app']/div/div/div/div[2]/div/form/fieldset/div[3]/button").click() #로그인