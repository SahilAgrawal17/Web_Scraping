import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys

def open_leetcode_problem(link):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(link)

    try:
        wait = WebDriverWait(driver, 10)
        difficulty_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.text-difficulty-easy, .text-difficulty-medium, .text-difficulty-hard')))
        difficulty = "Unknown"
        if 'Easy' in difficulty_element.text:
            difficulty = "Easy"
        elif 'Medium' in difficulty_element.text:
            difficulty = "Medium"
        elif 'Hard' in difficulty_element.text:
            difficulty = "Hard"

        print("Difficulty:", difficulty)

    except Exception as e:
        pass
    time.sleep(2)
    topics_button = driver.find_element(By.XPATH, "//div[text()='Topics']")
    topics_button.click()

    wait = WebDriverWait(driver, 10)
    topics_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.mt-2.flex.flex-wrap.gap-1.pl-7 a')))

    topics = [topic.text for topic in topics_elements]

    print("Topics:", topics)

    time.sleep(2)

if __name__ == "__main__":
    problem_link = input("Enter the LeetCode problem link: ")
    open_leetcode_problem(problem_link)