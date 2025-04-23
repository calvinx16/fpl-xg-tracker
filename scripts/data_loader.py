"""Fetch public data"""

# Load necessary packages
import pandas as pd
import requests

# Load data
def fetch_fpl_data():
    url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        players = pd.json_normalize(data['elements'])
        return players
    else:
        raise Exception("Failed to fetch FPL data")
