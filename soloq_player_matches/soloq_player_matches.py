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
#file = open("teams.txt", "w", encoding="utf-8")
driver.get("https://www.probuilds.net/teams/details/189")
file = open("soloq_team_matches.txt", "w", encoding='utf-8')
def load_more_games():
    time.sleep(1)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "moreMatchesButton"))
        )
        element.click()
    except:
        pass
    time.sleep(1)
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
    "player_id":[],
    "player_name":[],
    "team_id":[],
    "team":[],
    
}
dataset1 = {
    "player_id" : [],
    "player_name" : [],


}

player_search = driver.find_element(By.CLASS_NAME, "pro-player-search-results")
players = player_search.find_elements(By.TAG_NAME, "li")
names = []
ids = []
for player in players:
    tag = player.find_element(By.TAG_NAME, "a")
    id = tag.get_attribute("href").split("/")[-1]
    name = tag.find_element(By.TAG_NAME, "h3")
    player_name = name.text
    ids.append(id)
    names.append(player_name)
    dataset["players_id"].append(ids)
    dataset["players"].append(players)

load_more_games()
holders = driver.find_elements(By.CLASS_NAME, "build-holder")
for holder in holders:
    block = holder.find_element(By.CLASS_NAME, "block")
    name_block = block.find_element(By.CSS_SELECTOR, ".player.gold")
    name_holder = name_block.find_element(By.CLASS_NAME, "gold")
    name = name_holder.text
    id = name_holder.get_attribute("href").split("/")[-1]
    file.write(name)
    file.write(id)
    champ_holder = block.find_element(By.CLASS_NAME, "champ")
    champ_img = champ_holder.find_element(By.TAG_NAME, "img")
    champ = champ_img.get_attribute("src").split("/")[-1].split(".")[0]
    print(champ)

    wins = block.find_elements(By.CLASS_NAME, "winborder")
    if len(wins)>0:
        win = "win"
    else:
        win = "lose"
    file.write(win + "\n")

        
driver.quit()