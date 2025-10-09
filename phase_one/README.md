# 🪙 Crypto Data Pipeline

A local **end-to-end ETL pipeline** for cryptocurrency market data built with **Apache Airflow**, **Python**, **SQLite**, and **Streamlit**.  
This project extracts real-time crypto prices from the **CoinGecko API**, transforms and stores them locally, and visualizes the results through an interactive dashboard — all running fully **offline** (no cloud required).

---

## 🚀 Project Overview

**Goal:**  
To demonstrate a local data engineering pipeline using open-source tools and free APIs.

**Stack:**
- **Airflow** – Orchestrates the ETL pipeline  
- **Python** – Handles data extraction, transformation, and loading  
- **SQLite** – Lightweight local database  
- **Streamlit** – Visualization and exploration dashboard  

---

## 🧩 Architecture

    ┌────────────────────┐
    │  CoinGecko API     │
    └───────┬────────────┘
            │
            ▼
    ┌────────────────────┐
    │  Extract (Python)  │
    └───────┬────────────┘
            │
            ▼
    ┌────────────────────┐
    │ Transform (Python) │
    └───────┬────────────┘
            │
            ▼
    ┌────────────────────┐
    │  Load (SQLite)     │
    └───────┬────────────┘
            │
            ▼
    ┌────────────────────┐
    │ Streamlit Dashboard│
    └────────────────────┘
## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/crypto-data-pipeline.git
cd crypto-data-pipeline
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🧠 Airflow Setup

### 1. Initialize Airflow (standalone)
```bash
airflow standalone
```

### 2. Create a symbolic link for the DAG

If your project is outside Airflow’s default folder:
```bash
ln -s /home/<user>/projects/phase_one/dags /home/<user>/airflow/dags/phase_one
```
And setup the filepaths on the src files.

### 3. Verify the DAG
```bash
airflow dags list
```
You should see: **crypto_etl_dag**

Then open the UI: http://localhost:8080

## 💾 Data Storage

The pipeline stores the output in:
```bash
/home/joel/projects/phase_one/database/crypto_data.db
```
To explore it manually:

```bash
sqlite3 data/crypto_data.db
sqlite> SELECT * FROM crypto_prices LIMIT 5;
```

## 📊 Visualization (Streamlit)

### Launch the dashboard:
```bash
streamlit run streamlit_app.py
```

### The app connects to crypto_data.db and displays:
* Current top 5 cryptocurrencies by market cap
*  Price and market cap trends
*  Data refresh timestamps

### 🧰 Key Concepts Demonstrated
* ETL orchestration with Airflow DAGs
* Task communication using XComs (ti.xcom_pull)
* Modular code organization (src/ pattern)
* Local persistence via SQLite
* Lightweight visualization using Streamlit

### 🔮 Future Improvements
* Add Docker setup for reproducibility
* Include data validation with Great Expectations
* Schedule historical trend analysis
* Migrate to a cloud data warehouse (e.g. BigQuery or Snowflake)

---
# 🧑‍💻 Author
Joel Adid Rivas Mata
Senior Data Scientist | Data Engineer | Cloud Architect
LinkedIn | GitHub
