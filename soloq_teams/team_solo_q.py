from this import d
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "chromedriver.exe"
PATH1 = "chromedriver1.exe"
driver = webdriver.Chrome(PATH)
s_driver = webdriver.Chrome(PATH1)
#file = open("teams.txt", "w", encoding="utf-8")
driver.get("https://www.probuilds.net/teams")
dataset = {
    "team_id":[],
    "team_name":[],
    "region":[],
    "players":[],
    "wins":[],
    "loses":[]
}
regions_name = ["North America", "Europe", "Korea", "Brazil", "Oceania", "Turkey"]

for i in range(len(regions_name)):
    regions = driver.find_elements(By.CLASS_NAME, "specific-team")
    teams = regions[i].find_elements(By.TAG_NAME, "a")
    for team in teams:
        regions = driver.find_elements(By.CLASS_NAME, "specific-team")
        teams = regions[i].find_elements(By.TAG_NAME, "a")
        id = team.get_attribute("href").split("/")[-1]
        team_name = team.text
        dataset['team_id'].append(id)
        dataset['team_name'].append(team_name)
        dataset['region'].append(regions_name[i])
        time.sleep(3)
        s_driver.get("https://www.probuilds.net/teams/details/" + str(id))
        print(driver.find_elements(By.CLASS_NAME, "specific-team"))
        


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

#for i in range(10):
#    load_more_games()


#blocks = driver.find_elements(By.CLASS_NAME, "block")
#for block in blocks:
#    file.write(block.text)
driver.close()
