

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     # without warning
#driver = webdriver.Chrome(ChromeDriverManager().install())                     ::2nd Chance
#driver=webdriver.Chrome(executable_path="D:\BrowserDrivers\chromedriver.exe")  :::3rd Chance

driver.get("http://127.0.0.1/orangehrm-2.6/login.php");
print(driver.title);
print(driver.current_url);
time.sleep(5)

ele2=driver.find_element('xpath', '//input[@name="Submit"]')
#ele1=driver.find_element(By.Name, 'Submit')
print(ele2.is_displayed())

driver.find_element('xpath', '//input[@name="txtUserName"]').send_keys("nareshit")
driver.find_element('xpath', '//input[@name="txtPassword"]').send_keys("nareshit")

ele2.click()
time.sleep(5)
driver.close();
#driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]')
