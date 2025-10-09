import os
import requests
import json
from datetime import datetime
from pathlib import Path

RAW_DATA_PATH = '/home/joel/Documents/data_engineering/phase_one/data/raw'


def extract_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order":"market_cap_desc",
        "per_page":"10",
        "page":1,
        "sparkline":False
        }
    response = requests.get(url, params=params)
    data = response.json()

    filename = f"{RAW_DATA_PATH}/crypto_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    
    return str(filename)


if __name__ == '__main__':
    print(extract_data())