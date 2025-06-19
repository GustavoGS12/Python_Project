import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.youtube.com/watch?v=QMI309FP3OI"


driver = webdriver.Chrome()

i = 0
while i < 5:
    i += 1
    driver.get(url)
    time.sleep(30)
    driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[26]/div[2]/div[1]/button').click()
    time.sleep(160)
