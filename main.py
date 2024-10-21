from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

settings = [1, 0, 0, 1, 2, 4, 4, 1, 0, 0, 2, -1, 0, 1, -1, 0, 2, 0, 0, 0]

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=Options())

driver.get("https://hashtagbasketball.com/fantasy-basketball-points-league-rankings")
driver.maximize_window()

inputs = driver.find_elements("xpath", "//input[@type='text']")

for input, value in zip(inputs, settings):
    input.clear()
    input.send_keys(str(value))

driver.find_element("xpath", "//input[@type='submit']").click()

driver.quit()