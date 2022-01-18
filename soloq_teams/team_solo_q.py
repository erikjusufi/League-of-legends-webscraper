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
dataset = {
    "team_id":[],
    "team_name":[],
    "region":[],
    "players_id": [],
    "players":[],
    "wins":[],
    "loses":[]
}
players = {
    "player_id",
    "player_name"
}
dataset1 = {
    "player_id" : [],
    "player_name" : [],


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
        player_search = s_driver.find_element(By.CLASS_NAME, "pro-player-search-results")
        players = player_search.find_elements(By.TAG_NAME, "li")
        names = []
        ids = []
        for player in players:
            val = player.find_element(By.TAG_NAME, "a")
            id = val.get_attribute("href").split("/")[-1]
            name = val.text
            id.append(id)
            names.append(name)
        dataset["players_id"].append(ids)
        dataset["players"].append(players)
        load_more_games()
        blocks = driver.find_elements(By.CLASS_NAME, "block")
        for block in blocks:
            win = block.find_element(By.CLASS_NAME, "winborder")
            if win == None:
                win = "lose"
            else:
                win = "win"
            print(win)
            

        




#for i in range(10):
#    load_more_games()


#blocks = driver.find_elements(By.CLASS_NAME, "block")
#for block in blocks:
#    file.write(block.text)
driver.close()
s_driver.close()
