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

page = requests.get("https://www.probuilds.net/pros")
soup = BeautifulSoup(page.text, 'lxml')
entries = soup.find_all("tr", class_="pro-player-entry")
for entry in entries:
    r = entry.find("a")
    name = r.text.strip()
    dataset['name'].append(name)
    r = entry.find("td", class_="win_per dark")
    win_per = r.text
    dataset['win_per'].append(win_per)
    r = entry.find("td", class_="wins light green")
    wins = r.text
    dataset['wins'].append(wins)
    r = entry.find("td", class_="losses dark red")
    loses = r.text
    dataset['losses'].append(loses)
    num_of_games = int(wins) + int(loses)
    dataset['num_of_games'].append(num_of_games)
    r = entry.find("td", class_="rank light")
    rank = r.text
    dataset['rank'].append(rank)
    r = entry.find("span", class_="green")
    kills = r.text
    dataset['kills'].append(kills)
    r = entry.find("span", class_="red")
    deaths = r.text
    dataset['deaths'].append(deaths)
    r = entry.find("span", class_="yellow")
    assists = r.text
    dataset['assists'].append(assists)
    kda = (int(kills) + int(assists))/int(deaths)
    dataset['kda'].append(kda)
    r = entry.find("td", class_="server light")
    server = r.text
    dataset['server'].append(server)
    data = entry.get("data-text").split("|")
    id = data[0]
    dataset['id'].append(id)
    real_name = data[1]
    dataset['real_name'].append(real_name)

df = pd.DataFrame(dataset)
df.to_csv('pro_players.csv')


    