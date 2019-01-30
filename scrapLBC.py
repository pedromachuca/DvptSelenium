from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.leboncoin.fr")
#elem = driver.find_elements_by_class_name("_3mctU")
links=driver.find_element_by_xpath("/html/body/div/div/div/span[1]/section/main/div/div/section[1]/div/div[1]/div[2]/section/div[2]/ul/li[6]/a")
test=links.get_attribute('href') 
driver.get(test)
title=driver.find_elements_by_xpath('//section/div/p/span')
for l in title:
    print l.text
