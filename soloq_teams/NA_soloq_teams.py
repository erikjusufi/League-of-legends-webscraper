from os import times
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
s_driver = webdriver.Chrome(PATH1)
#file = open("teams.txt", "w", encoding="utf-8")
driver.get("https://www.probuilds.net/teams")
def load_more_games():
    time.sleep(1)
    try:
        element = WebDriverWait(s_driver, 10).until(
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
regions_name = ["North America", "Europe", "Korea", "Brazil", "Oceania", "Turkey"]

for i in range(1):
    regions = driver.find_elements(By.CLASS_NAME, "specific-team")
    print(len(regions))
    teams = regions[i].find_elements(By.TAG_NAME, "a")
    for team in teams:
        regions = driver.find_elements(By.CLASS_NAME, "specific-team")
        teams = regions[i].find_elements(By.TAG_NAME, "a")
        team_id = team.get_attribute("href").split("/")[-1]
        team_name = team.text
        print(team)
        dataset['team_id'].append(team_id)
        dataset['team_name'].append(team_name)
        dataset['region'].append(regions_name[i])
        time.sleep(1)
        s_driver.get("https://www.probuilds.net/teams/details/" + str(team_id))
        player_search = s_driver.find_element(By.CLASS_NAME, "pro-player-search-results")
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
            data_player["team"].append(team_name)
            data_player["team_id"].append(team_id)
        dataset["players_id"].append(ids)
        dataset["players"].append(names)    

        num_win = 0
        num_loss = 0
        for j in range(3):
            load_more_games()
        holders = s_driver.find_elements(By.CLASS_NAME, "build-holder")
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
        dataset["loses"].append(num_loss)
        dataset["wins"].append(num_win)
    

            

        




#for i in range(10):
#    load_more_games()


#blocks = driver.find_elements(By.CLASS_NAME, "block")
#for block in blocks:
#    file.write(block.text)

df = pd.DataFrame(dataset)
df.to_csv('team_soloq.csv')
df1 = pd.DataFrame(matches)
df1.to_csv('soloq_matches.csv')
df2 = pd.DataFrame(data_player)
df2.to_csv('players_teams.csv')
driver.close()
s_driver.close()
