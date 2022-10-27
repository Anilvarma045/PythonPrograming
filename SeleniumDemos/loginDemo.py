from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # without warning
def login(usname, psword):

    driver.get("http://127.0.0.1/orangehrm-2.6/login.php")
    print("Application opned Successfully")
    driver.find_element('xpath', '//input[@name="txtUserName"]').send_keys(usname)
    driver.find_element('xpath', '//input[@name="txtPassword"]').send_keys(psword)
    driver.find_element('xpath', '//*[@name="Submit"]').click()
    driver.implicitly_wait(4)
    print("Application Opned Successfully")

def addEmployee(fname, lname):
    print("Add new Employee")
    driver.switch_to_frame("rightMenu")
    print("now we are in frame")
    driver.findElement('xpath','//input[@value="Add"]').click()
    driver.find_element('xpath', '//input[@id="txtEmpLastName"]').send_keys(lname)
    driver.find_element('xpath', '//input[@id="txtEmpFirstName"]').send_keys(fname)
    driver.find_element('xpath', '//input[@id="btnEdit"]').click()
    print("EMployee Added Successfully")

login("nareshit", "nareshit")
addEmployee("Ramesh", "babu")

