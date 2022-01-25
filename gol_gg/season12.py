from os import times
from this import d
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

team_dataset = {
    "name": [],
    "season" : [],
    "region" : [],
    "games" : [],
    "win rate": [],
    "k:d" : [],
    "gold per min": [],
    "gold diff per min": [],
    "game duration" : [],
    "kill per game": [],
    "deaths per game" : [],
    "towers killed": [],
    "towers lost": [],
    "first blood rate": [],
    "first tower rate": [],
    "dragons per game": [],
    "dragons %" : [],
    "heralds per game": [],
    "herald %" : [],
    "avg dragons 15min" : [],
    "tower diff 15min" : [],
    "gold diff 15min": [],
    "nashor per game": [],
    "nashor %": [],
    "cs per min": [],
    "dmg per min": [],
    "wards per min": [],
    "vision wards per min": [],
    "wards cleared per min": [],


}
PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
#file = open("output.txt", "w", encoding="utf-8")
driver.get("https://gol.gg/teams/list/season-S10/split-ALL/tournament-ALL/")
season_table = driver.find_element(By.TAG_NAME, "tbody")
table = driver.find_element(By.CLASS_NAME, "table_list")

teams = table.find_elements(By.TAG_NAME, "tr")
for team in teams:
    pass
    ats = team.find_elements(By.TAG_NAME, "td")
    for at,key in zip(ats, team_dataset.keys()):
        print(key, ":", at.get_attribute("textContent"))
        team_dataset[key].append(str(at.get_attribute("textContent")))



df = pd.DataFrame(team_dataset)
df.to_csv('season10.csv')
driver.close()
#file.close()
