import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException

def extract_topics_and_rating(link):
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(link)
    time.sleep(4)
    try:
        topics_elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.tag-box'))
        )
        topics = [topic.text.strip() for topic in topics_elements if "Difficulty" not in topic.get_attribute("title")]

    except TimeoutException:
        print("Timeout occurred while waiting for topics.")
        topics = []

    try:
        rating_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-box[title="Difficulty"]'))
        )

        rating = rating_element.text.strip('*')
    except TimeoutException:
        print("Timeout occurred while waiting for difficulty rating.")
        rating = "Unknown"

    return topics, rating

if __name__ == "__main__":
    codeforces_link = input("Enter the Codeforces problem link: ")
    topics, rating = extract_topics_and_rating(codeforces_link)

    print("Topics:", topics)
    print("Rating:", rating)
