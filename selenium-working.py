from selenium import webdriver
driver = webdriver.Firefox()
driver.get("http://www.google.com")
#print driver.page_source
driver.find_element_by_id('fname1').send_keys("realpython")
driver.find_element_by_name("enter-info").click()
driver.save_screenshot("s1.png")
driver.quit()
