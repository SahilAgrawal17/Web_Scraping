from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.leetcode.com/problemset/algorithms/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "h-5"))
)
input_element = driver.find_element(By.CLASS_NAME, "h-5")
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Valid Parentheses")
link.click()

# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Topics')]")))

# # Click on the "Topics" link
# topics_link = driver.find_element(By.XPATH, "//a[contains(text(),'Topics')]")
# topics_link.click()

# # Wait for the container holding topic names to be present
# WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "no-underline hover:text-current relative inline-flex items-center justify-center text-caption px-2 py-1 gap-1 rounded-full bg-fill-secondary text-text-secondary")))

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "text-sd-foreground"))
    )
time.sleep(4)
topic = driver.find_element(By.CLASS_NAME, "text-sd-foreground")
topic.click()


# print(topics.text)
time.sleep(10)
driver.quit()