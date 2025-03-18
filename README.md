# NCAA Basketball Game Predictor

This project predicts the outcomes of NCAA basketball games using statistical data scraped from Sports Reference. The project is split into two parts:
    1. A web scraper to pull historical and current team stats into a CSV. This only needs to run once. 
    2. A predictor script that analyzes the data and outputs game predictions.

## Dependencies
Make sure you have the following Python packages installed:
- `requests`
- `beautifulsoup4`
- `pandas`

Install them using command:
```pip install requests beautifulsoup4 pandas```

Or use command:
```pip install -r requirements.txt```

## How It Works
### scraper.py
The web scraper pulls team-level statistics (such as offensive and defensive efficiency) from the "School Stats" table
on the Sports Reference website and writes them into teams.csv. To pull stats for current season, navigate to its web page and copy and paste the url in scraper.py.

#### Run the scraper with command
```python scraper.py```

This outputs a teams.csv file in the current directory that contains all the necessary school stats for the season.

#### predictor.py
This script pulls two teams from commandline arguments and predicts their scores in a matchup using the information 
pulled from teams.csv. 
Note: Use the exact team names as they appear in teams.csv. If a name contains spaces, enclose it in quotation marks.

#### Run predictor.py with command
```python predictor.py {team 1 name} {team 2 name}```

## Example workflow
* Step 1: Scrape fresh data with command:
```python scraper.py```

* Step 2: Predict game outcomes for Montana and Nevada NCAA
```python predictor.py Montana "Nevada NCAA"```

## Future improvements
* Update scraper.py to take year from command line argument and automatically update URL to fetch correct year.
* Add unit tests for data scraping and prediction logic.
* Update prediction model. 

## Author
Sarah Bethea, 2025
