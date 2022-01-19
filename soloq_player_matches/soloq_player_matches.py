from this import d
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
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
data_player = {
    "player_id":[],
    "player_name":[],
    "team_id":[],
    "team":[],
    
}
matches = {
    "player_id" : [],
    "player_name" : [],
    "win_lose" : [],
    "champion1" : [],
    "champion2" : [],
    "kills" : [],
    "deaths" : [],
    "assists" : [],
    "gold" : [],
    "game_time" : [],
}
dataset['team_id'].append("no")
dataset['team_name'].append("no")
dataset['region'].append("no")
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

    data_player["player_id"].append(id)
    data_player["player_name"].append(player_name)
    data_player["team"].append("no")
    data_player["team_id"].append("no")

dataset["players_id"].append(ids)
dataset["players"].append(names)           

num_win = 0
num_loss = 0
for i in range(5):
    load_more_games()
holders = driver.find_elements(By.CLASS_NAME, "build-holder")
for holder in holders:
    block = holder.find_element(By.CLASS_NAME, "block")
    name_block = block.find_element(By.CSS_SELECTOR, ".player.gold")
    name_holder = name_block.find_element(By.CLASS_NAME, "gold")
    name = name_holder.text
    id = name_holder.get_attribute("href").split("/")[-1]
    matches["player_name"].append(name)
    matches["player_id"].append(id)

    champ_holder = block.find_element(By.CLASS_NAME, "champ")
    champ_img = champ_holder.find_element(By.TAG_NAME, "img")
    champ1 = champ_img.get_attribute("src").split("/")[-1].split(".")[0]
    champ_holder = block.find_element(By.CLASS_NAME, "opponent")
    champ_img = champ_holder.find_element(By.TAG_NAME, "img")
    champ2 = champ_img.get_attribute("src").split("/")[-1].split(".")[0]
    matches["champion1"].append(champ1)
    matches["champion2"].append(champ2)

    kda_holder = block.find_element(By.CLASS_NAME, "kda")
    kills = kda_holder.find_element(By.CLASS_NAME, "kill").text
    deaths = kda_holder.find_element(By.CLASS_NAME, "death").text
    assists = kda_holder.find_element(By.CLASS_NAME, "assists").text
    matches["kills"].append(kills)
    matches["deaths"].append(deaths)
    matches["assists"].append(assists)

    gold = block.find_element(By.CLASS_NAME, "_gold").text
    matches["gold"].append(gold)

    timestamp = block.find_element(By.CLASS_NAME, "time").text
    matches["game_time"].append(timestamp)

            
    wins = block.find_elements(By.CLASS_NAME, "winborder")
    if len(wins)>0:
        win = "win"
        num_win += 1
    else:
        win = "lose"
        num_loss += 1
    matches["win_lose"].append(win)
dataset["loses"] = num_loss
dataset["wins"] = num_win
df = pd.DataFrame(dataset)
df.to_csv('team_soloq.csv')
df1 = pd.DataFrame(matches)
df1.to_csv('soloq_matches.csv')
df2 = pd.DataFrame(data_player)
df2.to_csv('players_teams.csv')
driver.close()
        
driver.quit()