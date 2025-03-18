import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.sports-reference.com/cbb/seasons/2024-school-stats.html"

# Request the page using requests library.
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Directly locate the table. 
table = soup.find('table', {'id': 'basic_school_stats'})

# Extract data from the table rows.
data = []
for row in table.tbody.find_all('tr'):
    if row.get('class') and 'thead' in row.get('class'):
        continue  
    team = row.find('td', {'data-stat': 'school_name'}).text.strip()
    # Fix U+00A0 non-breaking space issue.
    team = team.replace('\xa0', ' ')
    # Remove " NCAA" from any team name
    team = team.replace(' NCAA', '')  

    games = float(row.find('td', {'data-stat': 'g'}).text.strip())
    sos = row.find('td', {'data-stat': 'sos'}).text.strip()

    pts = round(float(row.find('td', {'data-stat': 'pts'}).text.strip()) / games, 2)
    opp_pts = round(float(row.find('td', {'data-stat': 'opp_pts'}).text.strip()) / games , 2)
    mp = round(float(row.find('td', {'data-stat': 'mp'}).text.strip()) / games , 2)
    fg = round(float(row.find('td', {'data-stat': 'fg'}).text.strip()) / games , 2)
    fga = round(float(row.find('td', {'data-stat': 'fga'}).text.strip()) / games , 2)
    fg_pct = round(float(row.find('td', {'data-stat': 'fg_pct'}).text.strip()) / games , 2)
    fg3 = round(float(row.find('td', {'data-stat': 'fg3'}).text.strip()) / games , 2)
    fg3a = round(float(row.find('td', {'data-stat': 'fg3a'}).text.strip()) / games , 2)
    ft = round(float(row.find('td', {'data-stat': 'ft'}).text.strip()) / games , 2)
    fta = round(float(row.find('td', {'data-stat': 'fta'}).text.strip()) / games , 2)
    orb = round(float(row.find('td', {'data-stat': 'orb'}).text.strip()) / games , 2)
    tov = round(float(row.find('td', {'data-stat': 'tov'}).text.strip()) / games , 2)
    
    data.append([team, games, sos, pts, opp_pts, mp, fg, fga, fg_pct, fg3, fg3a, ft, fta, orb, tov])

# Save to CSV.
df = pd.DataFrame(data, columns=['team', 'games', 'sos', 'pts', 'opp_pts', 'mp', 'fg', 'fga', 'fg_pct', 'fg3', 'fg3a', 'ft', 'fta', 'orb', 'tov'])
df.to_csv('teams.csv', index=False)

print("Data scraped and saved to teams.csv")

