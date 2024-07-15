from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://korean.dict.naver.com/koendict/#/main"
driver = webdriver.Firefox()

try:
    # establish connection
    driver.get(url)

    # look for the conversation section
    conversation_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'todayQuiz'))
    )

    # get the sentence of the day
    origin_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'origin'))
    )
    origin_text = origin_element.text.strip()

    # get the translation for the sentence of the day
    translation_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'translate'))
    )
    translation_text = translation_element.text.strip()

    print("Today's Conversation (Korean):", origin_text)
    print("Today's Conversation (English):", translation_text)

finally:
    # shut down the driver
    driver.quit()
