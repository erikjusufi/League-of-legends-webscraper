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
file = open("champ.txt" ,"w", encoding='utf-8')
page = requests.get("https://www.op.gg/champion/statistics",  headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"})
soup = BeautifulSoup(page.text, 'lxml')
file.write(soup.prettify())

