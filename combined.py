import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def extract_topics_and_rating_codeforces(link):
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
        topics = []

    try:
        rating_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.tag-box[title="Difficulty"]'))
        )
        rating = rating_element.text.strip('*')

    except TimeoutException:
        rating = "Unknown"

    driver.quit()
    
    return topics, rating 

def extract_topics_and_rating_leetcode(link):
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

    except Exception as e:
        difficulty = "Unknown"

    time.sleep(2)

    try:
        topics_button = driver.find_element(By.XPATH, "//div[text()='Topics']")
        topics_button.click()
        wait = WebDriverWait(driver, 10)
        topics_elements = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.mt-2.flex.flex-wrap.gap-1.pl-7 a')))
        topics = [topic.text for topic in topics_elements]

    except Exception as e:
        print("Failed to extract topics:", e)
        topics = []

    time.sleep(2)
    driver.quit()

    return topics, difficulty 

def extract_topics_and_rating(link):
    if "leetcode.com" in link:
        return extract_topics_and_rating_leetcode(link)
    elif "codeforces.com" in link:
        return extract_topics_and_rating_codeforces(link)
    else:
        print("Unsupported website:", link)
        return None, None

if __name__ == "__main__":
    problem_link = input("Enter the problem link: ")
    topics, rating = extract_topics_and_rating(problem_link)

    if topics is not None and rating is not None:
        print("Topics:", topics)
        print("Rating:", rating)
