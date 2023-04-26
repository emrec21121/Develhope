# Exercise 1
# Add a last task which removes the dataset_raw.txt from the source folder

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_dag_args = {
    'start_date': datetime(2022, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'project_id': 1
}

with DAG("First_DAG", schedule_interval=None, default_args=default_dag_args) as dag:
    task_0 = BashOperator(task_id='bash_task', bash_command="echo 'command executed from Bash Operator'")
    task_1 = BashOperator(task_id='bash_task_move_data', bash_command="cp /Users/pedrocarneiro/peter/develhop/DATA_CENTER/DATA_LAKE/dataset_raw.txt  /Users/pedrocarneiro/peter/develhop/DATA_CENTER/CLEAN_DATA")
    task_2 = BashOperator(task_id='bash_task_move_data', bash_command="")
    task_3 = BashOperator(task_id='bash_task_remove_data', bash_command="rm /Users/pedrocarneiro/peter/develhop/DATA_CENTER/DATA_LAKE/dataset_raw.txt")
    
    task_0 >> task_1 >> task_2 >> task_3

# Exercise 2
# Create a dag with one python task only. This function should print the current datetime

from datetime import datetime, timedelta 
from airflow import DAG 
from airflow.operators.python import PythonOperator

def python_first_function(): 
    print(datetime.datetime.now())

default_dag_args = { 
    'start_date': datetime(2022, 9, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 
}

with DAG("first_python_dag", schedule_interval = None, default_args = default_dag_args) as dag_python:

    # here we define our tasks
    task_0 = PythonOperator(task_id = "first_python_task", python_callable = python_first_function)


# Exercise 3
# Write a DAG which is able to request market data for a list of stocks.

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from datetime import datetime, timedelta
import requests
import time
import json
import pandas as pd
import numpy as np 
import os

def get_data(**kwargs): 
    for ticker in kwargs:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={ticker}&apikey=<YOUR_API_KEY>'
        response = requests.get(url)
        data = response.json()
        df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
        df.to_csv(f'{ticker}.csv')

default_dag_args = { 
    'start_date': datetime(2022, 9, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 
}

with DAG("market_data_alphavantage_dag", schedule_interval = '@daily', catchup=False, default_args = default_dag_args) as dag_python:
    task_0 = PythonOperator(task_id = "get_market_data", python_callable = get_data, op_kwargs = {'tickers' : ["IBM", "AAPL"]})

# Exercise 4
# Write a DAG which creates an employe table - each row represents a new person and contains info about their name and age then insert 3 people (with the correct metadata) finally execute a query which calculates the average age of all employees

# pip install apache-airflow-providers-postgres
import time 
import json 
from airflow import DAG 
from airflow.operators.postgres_operator import PostgresOperator 
from datetime import timedelta
from airflow.utils.dates import days_ago

default_dag_args = { 
    'start_date': datetime(2022, 9, 1), 
    'email_on_failure': False, 
    'email_on_retry': False, 
    'retries': 1, 
    'retry_delay': timedelta(minutes=5), 
    'project_id': 1 
}

# Create the employee table
create_query = """CREATE TABLE IF NOT EXISTS employee (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL
);"""

# Insert some data into the employee table
insert_data_query = """INSERT INTO employee (name, age) VALUES
  ('John Doe', 30),
  ('Jane Smith', 25),
  ('Bob Johnson', 40);"""

# Calculate the average age of all employees
calculating_average_age = """SELECT AVG(age) AS avg_age FROM employee;"""

dag_postgres = DAG(dag_id = "postgres_dag_connection", default_args = default_dag_args, schedule_interval = None, start_date = days_ago(1))

create_table = PostgresOperator(task_id = "creation_of_table", sql = create_query, dag = dag_postgres, postgres_conn_id = "postgres_pedro_local")

insert_data = PostgresOperator(task_id = "insertion_of_data", sql = insert_data_query, dag = dag_postgres, postgres_conn_id = "postgres_pedro_local")

group_data = PostgresOperator(task_id = "calculating_averag_age", sql = calculating_average_age, dag = dag_postgres, postgres_conn_id = "postgres_pedro_local")

create_table >> insert_data >> group_data