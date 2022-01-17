from tarfile import RECORDSIZE
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

dataset = {
    'id':[],
    'name':[],
    'real_name':[],
    'win_per':[],
    'wins':[],
    'losses':[],
    'num_of_games':[],
    'rank':[],
    'kills':[],
    'deaths':[],
    'assists':[],
    'kda':[],
    'server':[]
}

file = open("player_games/output.txt", "w", encoding="utf-8")
dt = pd.read_csv("player_stats/pro_players.csv")
page = requests.get("https://www.probuilds.net/pros/details/6038")
soup = BeautifulSoup(page.text, 'lxml')
file.write(soup.prettify())
entries = soup.find("div", class_="champ")
print(entries)
