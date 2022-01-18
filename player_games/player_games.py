from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
file = open("player_games.txt", "w", encoding="utf-8")
driver.get("https://www.probuilds.net/pros/details/6416")

def load_more_games():
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "moreMatchesButton"))
        )
        element.click()
    except:
        pass

    time.sleep(2)

for i in range(10):
    load_more_games()


blocks = driver.find_elements(By.CLASS_NAME, "block")
for block in blocks:
    file.write(block.text)
driver.close()
file.close()