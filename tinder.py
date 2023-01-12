import time
from selenium.webdriver.common.by import By
from selenium import webdriver

phone_number = 7207885507

browser = webdriver.Chrome('webdriver.exe')
browser.get('https://www.tinder.com')
time.sleep(2)

#check if cookie popup exists
l = browser.find_elements(By.XPATH, '//*[@id="o-1773584476"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]') 
s = len(l)
if s > 0:
    print("Popup detected.")
    cookies = browser.find_element(By.XPATH, '//*[@id="o-1773584476"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
    cookies.click()
    print("Popup removed!")
else:
    print("No popup detected.")

login = browser.find_element(By.XPATH, '//*[@id="o-1773584476"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(2)

with_phone = browser.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]')
with_phone.click()
time.sleep(5)

enter_phone_number = browser.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/div[2]/div/input')
enter_phone_number.send_keys(phone_number)

continue_button = browser.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/button/div[2]/div[2]')
continue_button.click()

time.sleep(1)

code = input("Enter Code")
enter_code = browser.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/div[3]/input[1]')
enter_code.send_keys(code)

continue_button = browser.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/button/div[2]/div[2]')
continue_button.click()

time.sleep(1)

code = input("Enter Code")
enter_code = browser.find_element(By.XPATH, '//*[@id="o793001744"]/main/div/div[1]/div/div[3]/input[1]')
enter_code.send_keys(code)

time.sleep(1000)