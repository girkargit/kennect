import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
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

def discount_verifiyer(data, per, total):
    """
    Discount verification
    """
    print(data, per, total)
    percentage = (data / 100) * per
    op = data - percentage
    print(op)
    if op == total:
        print("test case pass")
    else:
        print("test case fail")



def cost_calculator_for_blood_test():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, "//div[@role='combobox']//button[@title='Open']").click()
    time.sleep(2)
    txt_1 = driver.find_element(By.XPATH, "//div[@id='patient-test-popup']/ul/li[1]/div").text
    driver.find_element(By.XPATH, "//div[@id='patient-test-popup']/ul/li[1]/div").click()
    driver.find_element(By.XPATH, "//div[@role='combobox']//button[@title='Open']").click()
    time.sleep(2)
    txt_2 = driver.find_element(By.XPATH, "//div[@id='patient-test-popup']/ul/li[2]/div").text
    driver.find_element(By.XPATH, "//div[@id='patient-test-popup']/ul/li[2]/div").click()
    driver.find_element(By.XPATH, "//div[@aria-haspopup='listbox']").click()
    per = driver.find_element(By.XPATH, "//ul[@role='listbox']/li[3]").text
    driver.find_element(By.XPATH, "//ul[@role='listbox']/li[3]").click()
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    total = driver.find_element(By.XPATH, "//div[@class='MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded']/div/div[3]/div[2]/div[2]").text
    add = txt_1.split("\n")[-1]
    x = add.split("₹")[0]
    add_1 = txt_2.split("\n")[-1]
    y = add_1.split("₹")[0]
    xp = int(x) + int(y)
    val = per.split('%')[0]
    tot = total.split("₹")[0]
    discount_verifiyer(xp, int(val), int(tot))

logoin()
cost_calculator_for_blood_test()