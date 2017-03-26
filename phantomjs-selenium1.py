from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
driver.set_window_size(1120, 550)
driver.get("http://strontium.shape/boxuan/simple-welcome-post.php")
driver.save_screenshot("s1.png")
driver.find_element_by_id('fname1').send_keys("realpython")
driver.find_element_by_name("signIn").click()
print driver.current_url
driver.save_screenshot("s1.png")
driver.quit()
