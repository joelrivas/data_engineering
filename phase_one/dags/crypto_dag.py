import os
import sys
from pathlib import Path
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

DAG_FOLDER = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.join(DAG_FOLDER, '..')
sys.path.append(PROJECT_ROOT)

from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data


DAG_args = {
    "dag_id": "crypot_etl_dag",
    "default_args": {
        "owner": "Joel Rivas",
        "depends_on_past":False,
        "start_date": datetime(2025,10,6),
        "retries": 1,
        "retry_delay": timedelta(minutes=5)
    },
    "schedule": timedelta(days=1),
    "catchup": False
}

def extract_task():
    print("Iniciando Extraccion")
    filename = extract_data()
    print("Extraccion Completada")
    return filename
    
def transform_task(ti):
    data = ti.xcom_pull(task_ids="extract")
    df = transform_data(data)
    return df
    
def load_task(ti):
    df = ti.xcom_pull(task_ids="transform")
    load_data(df)


with DAG(**DAG_args) as dag:
    extract = PythonOperator(task_id="extract", python_callable=extract_task)
    transform = PythonOperator(task_id="transform", python_callable=transform_task)
    load = PythonOperator(task_id="load", python_callable=load_task)

    extract >> transform >> load
