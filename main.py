import time
from selenium import webdriver

# enter the path where browser driver is installed on your machine
webdriverPath = 'C:/Users/layea/Downloads/chromedriver_win32/chromedriver'
driver = webdriver.Chrome(webdriverPath) 

driver.get('http://www.google.com/');

time.sleep(5) # Let the user actually see something!

search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!

driver.quit()