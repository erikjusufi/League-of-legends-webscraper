from tarfile import RECORDSIZE
import requests
from bs4 import BeautifulSoup
import pandas as pd

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
dt = pd.read_csv("../player_stats/pro_players.csv")
for id in dt['id']: 
    page = requests.get("https://www.probuilds.net/pros/details/6038")
    soup = BeautifulSoup(page.text, 'lxml')
    entries = soup.find_all("div", id_="pro-player-feed-5")
    



    