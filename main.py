import pandas as pd
import requests
from bs4 import BeautifulSoup

QB_raw = pd.read_csv("QBout.csv").set_index("Player")

player_list = 

#Make the link column the complete link
QB_raw["Link"] = ["http://www.nfl.com/"+i+"gamelogs?season=2019" for i in QB_raw["Link"].tolist()]

page = requests.get(QB_raw.loc["Allen, Brandon", "Link"])

soup = BeautifulSoup(page.content, 'html.parser')

headings = [heading.get_text() for heading in soup.find("tr", class_ = "player-table-key").find_all("td")]
print(headings)

#for output in outputs.find_all("td"):
  #print(output)