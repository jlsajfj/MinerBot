from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
start_url = "https://ethermine.org/miners/3e7AEF011a4b792C707d4ecA232C310B911A9dF7/dashboard"
driver.get(start_url)
print(driver.page_source.encode("utf-8"))
driver.quit()