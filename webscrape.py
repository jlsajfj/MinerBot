from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, time

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)
start_url = "https://ethermine.org/miners/3e7AEF011a4b792C707d4ecA232C310B911A9dF7/dashboard"
driver.get(start_url)
assert "Dashboard" in driver.title
time.sleep(1)

# (//div[@class="stat-card-body"])[1]/span[1]
# .current-earnings
# .current-balance

xpath = driver.find_element_by_xpath
class_name = driver.find_element_by_class_name

cur_earnings = class_name('current-earnings').text
cur_balance  = class_name('current-balance').text

cur_hashrate = xpath('(//div[@class="stat-card-body"])[1]/span[1]').text
avg_hashrate = xpath('(//div[@class="stat-card-body"])[2]/span[1]').text
rep_hashrate = xpath('(//div[@class="stat-card-body"])[3]/span[1]').text

print("Current Earnings:  {} ETH".format(cur_earnings))
print("Current Balance:   {} ETH".format(cur_balance))
print("Current Hashrate:    {} MH/s".format(cur_hashrate))
print("Average Hashrate:    {} MH/s".format(avg_hashrate))
print("Reported Hashrate:   {} MH/s".format(rep_hashrate))

data = {
    "cur_earnings": cur_earnings,
    "cur_balance": cur_balance,
    "cur_hashrate": cur_hashrate,
    "avg_hashrate": avg_hashrate,
    "rep_hashrate": rep_hashrate
}

print(data)

# print(driver.page_source.encode("utf-8"))
driver.quit()