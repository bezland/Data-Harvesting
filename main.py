import pandas as pd
import requests
from bs4 import BeautifulSoup

#Set Headings
QB_headings = ["WK", "Game Date", "Opp", "Result", "G", "GS", "P-Comp", "P-Att", "P-Pct", "P-Yds", "P-Avg", "P-TD", "Int", "Sck", "SckY", "Rate", "R-Att", "R-Yds", "R-Avg", "R-TD", "FUM", "Lost"]
RB_headings = ["WK", "Game Date", "Opp", "Result", "G", "GS", "R-Att", "R-Yds", "R-Avg", "R-Lng", "R-TD", "Rec", "Re-Yds", "Re-Avg", "Re-Lng", "FUM", "Lost"]
WR_headings = ["WK", "Game Date", "Opp", "Result", "G", "GS", "P-Comp", "P-Att", "P-Pct", "P-Yds", "P-Avg", "P-TD", "Int", "Sck", "SckY", "Rate", "R-Att", "R-Yds", "R-Avg", "R-TD", "FUM", "Lost"]
TE_headings = ["WK", "Game Date", "Opp", "Result", "G", "GS", "P-Comp", "P-Att", "P-Pct", "P-Yds", "P-Avg", "P-TD", "Int", "Sck", "SckY", "Rate", "R-Att", "R-Yds", "R-Avg", "R-TD", "FUM", "Lost"]

QB_raw = pd.read_csv("QBout.csv").set_index("Player")

#player_list =

#Make the link column the complete link
QB_raw["Link"] = ["http://www.nfl.com/"+i+"gamelogs?season=2019" for i in QB_raw["Link"].tolist()]

#page = requests.get(QB_raw.loc["Allen, Brandon", "Link"])

#soup = BeautifulSoup(page.content, 'html.parser')

#headings = [heading.get_text() for heading in soup.find("tr", class_ = "player-table-key").find_all("td")]

