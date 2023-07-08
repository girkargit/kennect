import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service= service_obj )
driver.implicitly_wait(5)
driver.get("https://gor-pathology.web.app/")
driver.maximize_window()

def logoin():
    """
    Login process : Checking login process.
    """
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("test@kennect.io")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwerty@1234")
    driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
    # checking for if is it landing on proper home page.
    text = driver.find_element(By.XPATH, "//div[@class='title']").text
    assert text == "Dashboard"

def read_data_from_csv(file_name):
    lst = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            lst.append(row)
    return lst

def scroll():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def adding_patients_and_creating_tests():
    driver.find_element(By.XPATH, "//span[text()='Patients']").click()
    driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
    # Add pateint with normal details
    data = read_data_from_csv(r"C:\Users\abhil\Downloads\xpath_test_case.csv")
    for xp in data:
        for xpath in xp[1:]:
            if xpath.split('|')[0] == "click":
                driver.find_element(By.XPATH, xpath.split('|')[1]).click()
            elif xpath == "scroll":
                scroll()
            else:
                op = xpath.split('|')
                driver.find_element(By.XPATH, op[1]).send_keys(op[2])
            time.sleep(1)

    # Check if it id pateint is added or not.
    lst = driver.find_elements(By.XPATH, "//table[@class='MuiTable-root']/tbody/tr")
    for i in lst:
        txt = i.text
        # Pateint name
        if "test" in txt:
            print("Pateint is present.")

logoin()
adding_patients_and_creating_tests()

