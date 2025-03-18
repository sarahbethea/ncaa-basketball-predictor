# NCAA Basketball Game Predictor

This project predicts the outcomes of NCAA basketball games using statistical data scraped from Sports Reference. The project is split into two parts:
    1. A web scraper to pull historical and current team stats into a CSV. This only needs to run once. 
    2. A predictor script that analyzes the data and outputs game predictions.

The prediction model adjusts for pace, offensive and defensive efficiency, and KenPom-style weights for shooting, turnovers, rebounding, and free throws — while also factoring in schedule strength and randomness. The output is a predicted final score for both teams in a given matchup. Its key components include:
##### Adjusted Tempo:
Each team’s tempo is calculated using their per-game averages (FGA, FTA, ORB, TOV, and MP). Then both teams' tempos are combined to create an adjusted tempo for the matchup.
##### Adjusted Offensive Efficiency (Adjusted OE):
Each team’s Offensive Efficiency (points per 100 possessions) is adjusted based on their opponent’s Defensive Efficiency, and by comparing both teams’ efficiencies to NCAA D1 averages. This creates a matchup-specific Adjusted OE.
##### KenPom-inspired 4 Factors Adjustment:
Following a KenPom-style approach, the two teams are compared using four key statistical factors. Each factor is computed as a difference between the two teams and weighted accordingly to create a factor adjustment that slightly boosts or penalizes each team's predicted score. The four factor and their weights are as follows:
* 40% Effective Field Goal % (eFG%)
* 25% Turnover % (TO%)
* 20% Offensive Rebound % (OR%)
* 15% Free Throw Rate (FT Rate)
##### Strength of Schedule (SOS) Adjustment:
To reward teams to have faced tougher opponents during the season, a boost is applied to each team's score based on their Strength of Schedule (SOS).
##### Luck Factor:
To simulate real-world variance, we introduce a random "luck" factor for each team, which randomly adds or subtracts up to 2 points.

## Dependencies
Make sure you have the following Python packages installed:
- `requests`
- `beautifulsoup4`
- `pandas`

Install them using command:
```bash
pip install requests beautifulsoup4 pandas
```

Or use command:
```bash 
pip install -r requirements.txt
```

## How It Works
### scraper.py
The web scraper pulls team-level statistics (such as offensive and defensive efficiency) from the "School Stats" table
on the Sports Reference website and writes them into teams.csv. To pull stats for current season, navigate to its web page and copy and paste the url in scraper.py.

#### Run the scraper with command
```bash
python scraper.py
```

This outputs a teams.csv file in the current directory that contains all the necessary school stats for the season.

#### predictor.py
This script pulls two teams from commandline arguments and predicts their scores in a matchup using the information 
pulled from teams.csv. 
##### Note: Use the exact team names as they appear in teams.csv. If a name contains spaces, enclose it in quotation marks, as shown in example workflow below.

#### Run predictor.py with command
```bash
python predictor.py {team 1 name} {team 2 name}
```

## Example workflow
* Step 1: Scrape fresh data with command:
```bash
python scraper.py
```

* Step 2: Predict game outcomes for Montana and Northern Arizona
```bash
python predictor.py Montana "Northern Arizona"
```

## Future improvements
* Update scraper.py to take year from command line argument and automatically update URL to fetch correct year.
* Add unit tests for data scraping and prediction logic.
* Update prediction model. 

## Author
Sarah Bethea, 2025
