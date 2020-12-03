from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.msn.com')
driver.find_element_by_xpath('//*[@id="main"]/div[6]/ul/li[6]/a/img[1]').click()

