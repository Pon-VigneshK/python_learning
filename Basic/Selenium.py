import selenium
from selenium.webdriver.chrome import webdriver

driver = webdriver.Chrome()

driver.get("http://selenium.dev")

driver.quit()
