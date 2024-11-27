from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the Python function to be executed
def hello_world():
    print("Hello, World! Schduled every 30 seconds")
    print(f"Current Time: {datetime.now()}")
    return "Example Returned Value"
# Define the DAG (Directed Acyclic Graph)
dag = DAG(
    'hello_task_schedule_every_30s',  # Name of the DAG
    description='An example DAG to print Hello World every 30 seconds',
    schedule_interval='*/1 * * * *',  # Run every minute (this is the minimum with schedule_interval)
    start_date=datetime(2024, 1, 1),  # Start date of the DAG
    catchup=False,  # To prevent running past missed intervals
)

# Define the task
task = PythonOperator(
    task_id='hello_task_schedule_every_30s',
    python_callable=hello_world,  # Function to execute
    dag=dag,
)
