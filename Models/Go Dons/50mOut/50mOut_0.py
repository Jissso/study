# Import modules
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import json

# Fetch webpage and response
url = 'https://www.wheeloratings.com/afl_match_stats.html?ID=20241103'
response = requests.get(url)

if response.status_code == 200:
    page_content = response.text
else:
    print("Failed to retrieve the webpage")

# Parse HTML (webpage) content and find table
soup = BeautifulSoup(page_content, 'html.parser')

# Locate the script tag
script_tag = soup.find('script', {'id': 'application/json', 'data-for': 'htmlwidget-stats-team'})

if script_tag:
    json_data = script_tag.string
    data = json.loads(json_data)
    # Now `data` contains the parsed JSON data
else:
    print("Script tag with JSON data not found")