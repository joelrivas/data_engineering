import os
import pandas as pd
import sqlite3

DATABASE_PATH = '/home/joel/Documents/data_engineering/phase_one/database'


def load_data(filename, testing=False):
    conn = sqlite3.connect(f"{DATABASE_PATH}/crypto_data.db")
    
    df = pd.read_csv(filename)
    if testing:
        table_name = "crypto_prices_test"
    else:
        table_name = "crypto_prices"
    df.to_sql(table_name, conn, if_exists="append", index=False)
    conn.close()


if __name__ == "__main__":
    load_data("/home/joel/Documents/data_engineering/phase_one/data/processed/crypto_clean_test.csv", True)