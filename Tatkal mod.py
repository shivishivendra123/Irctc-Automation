from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait
import time

#cap = DesiredCapabilities().FIREFOX
#cap["marionette"] = False
#binary = FirefoxBinary('C:\Program Files\Mozilla Firefox\firefox.exe')
#driver = webdriver.Firefox(capabilities=cap, executable_path=r"C:\geckodriver.exe",firefox_binary=binary)
driver = webdriver.Chrome("C:\chromedriver.exe")

driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(10)
driver.maximize_window()
elem = WebDriverWait(driver,60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="userId"]'))
    )
elem.send_keys("shivnikki")
#userid = driver.find_element_by_css_selector('input[name="userId"]').send_keys("shivnikki")
#pas = driver.find_element_by_css_selector('input[name="pwd"]').send_keys("Qwerty234")
elem = WebDriverWait(driver,60).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,'input[name="pwd"]'))
    )
elem.send_keys("Qwerty234")
time.sleep(20)
elem = WebDriverWait(driver,600).until(
        EC.element_to_be_clickable((By.XPATH,'//input[@placeholder="From*"]'))
    )
elem.click()
elem.send_keys("NEW DELHI - NDLS")
#forms = driver.find_element_by_xpath('//input[@placeholder="From*"]')
#forms.send_keys("NEW DELHI - NDLS")
forms = driver.find_element_by_xpath('//input[@placeholder="To*"]')
forms.send_keys("SHAHJEHANPUR - SPN")
driver.implicitly_wait(10)
forms = driver.find_element_by_xpath('//input[@placeholder="Journey Date(dd-mm-yyyy)*"]')
driver.implicitly_wait(10)
driver.implicitly_wait(10)

forms.clear()
forms.send_keys("31-01-2019")
forms.clear()
forms.send_keys("31-01-2019")
forms.send_keys(Keys.ENTER)
driver.maximize_window()
driver.maximize_window()
#r = WebDriverWait(driver,60).until(
#
 #       EC.visibility_of_elements_located((By.CSS_SELECTOR,"label[class='ng-tns-c13-13 ui-dropdown-label ui-inputtext ui-corner-all ng-star-inserted']"))
  #  )
#act = ActionChains(driver)
#act.move_to_element(r)
#act.send_keys("TATKAL")
#
#e = WebDriverWait(driver,60).until(

 #       EC.element_to_be_clickable((By.CSS_SELECTOR,"label[class='ng-tns-c13-13 ui-dropdown-label ui-inputtext ui-corner-all ng-star-inserted']"))
  #  )
#e.click()
#f = driver.find_element_by_css_selector("span[text='TATKAL']")

f = WebDriverWait(driver,600).until(

        EC.visibility_of_element_located((By.XPATH,"//span[text()='TATKAL']"))
    )
f.click()
WebDriverWait(driver,600).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"select[formcontrolname='classInput']"))
    ).send_keys("Sleeper(SL)")
m = driver.find_elements_by_css_selector('button[id="check-availability"]')[0].send_keys(Keys.ENTER)
#t = driver.find_elements_by_css_selector('button[type="submit"]')[0].send_keys(Keys.ENTER)
#element = WebDriverWait(driver,10).until(

 #       EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Check availability & fare')]"))
 #   ).text
#print(element)
#element = WebDriverWait(driver,10).until(

 #       EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Check availability & fare')]"))
  #  ).send_keys(Keys.ENTER)
#print(element)
#element.click()
element1 = WebDriverWait(driver,600).until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Book Now')]"))
    ).send_keys(Keys.ENTER)
#userid = driver.find_element_by_css_selector('input[name="userId"]').send_keys("shivnikki")
#pas = driver.find_element_by_css_selector('input[name="pwd"]').send_keys("Qwerty234")
#name = driver.find_element_by_css_selector('input[name="passengerName"]').send_keys("Qwerty")
#age = driver.find_element_by_css_selector('input[name="passengerAge"]').send_keys("67")
WebDriverWait(driver,60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"input[name='psgn-name']"))
    ).send_keys("Qwerty")
WebDriverWait(driver,60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"input[formcontrolname='passengerAge']"))
    ).send_keys("21")
WebDriverWait(driver,60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"select[formcontrolname='passengerGender']"))
    ).send_keys("Female")
WebDriverWait(driver,60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"select[formcontrolname='passengerBerthChoice']"))
    ).send_keys("Upper")

WebDriverWait(driver,60).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,"label[for='travelInsuranceOptedNo']"))
    ).click()
#WebDriverWait(driver,60).until(
       # EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Continue Booking')]"))
    #).send_keys(Keys.ENTER)



