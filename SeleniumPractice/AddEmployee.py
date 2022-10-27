from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service_obj=Service("D:\BrowserDriver\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.youtube.com/")

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(executable_path="D:/BrowserDrivers/chromedriver.exe")
driver.get("http://127.0.0.1/orangehrm-2.6/login.php")