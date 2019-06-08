from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(executable_path="C:/Users/LAL KRISHNA/PycharmProjects/08June2019/driver/chromedriver.exe")
driver.get("https://jqueryui.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_xpath('//*[@id="sidebar"]/aside[1]/ul/li[2]/a').click()
time.sleep(5)

driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="content"]/iframe'))
time.sleep(5)

source_element = driver.find_element_by_id("draggable")
destinatoin_element = driver.find_element_by_id("droppable")
time.sleep(5)

ActionChains(driver).drag_and_drop(source_element, destinatoin_element).perform()

