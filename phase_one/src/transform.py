import os
import json
import pandas as pd
from datetime import datetime

PROCESSED_DATA_PATH = '/home/joel/Documents/data_engineering/phase_one/data/processed'


def transform_data(filepath, testing=False):
    with open(filepath, "r") as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)[["id", "symbol", "current_price", "market_cap", "total_volume"]]
    df["extracted_at"] = pd.Timestamp.now()

    if testing:
        filename = f"{PROCESSED_DATA_PATH}/crypto_clean_test.csv"
    else:
        filename = f"{PROCESSED_DATA_PATH}/crypto_clean_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(filename, index=False)
    
    return str(filename)


if __name__ == "__main__":
    print(transform_data("/home/joel/Documents/data_engineering/phase_one/data/raw/crypto_test.json", True))