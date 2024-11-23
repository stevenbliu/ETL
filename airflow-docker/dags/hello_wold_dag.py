from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the Python function to be used in the task
def print_hello():
    print("Hello, World!")

# Initialize the DAGfrom airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Function to run your Python code
def hello_world():
    print("Hello from Airflow!")

# Define the DAG
dag = DAG('hello_airflow', description='A simple hello world DAG',
          schedule_interval='@once', start_date=datetime(2024, 11, 21), catchup=False)

# Define a task that will run the hello_world function
task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag,
)


with DAG(
    'hello_world_dag',
    default_args={
        'owner': 'airflow',
        'retries': 1,
    },
    description='A simple Hello World DAG',
    schedule_interval=None,  # None means the DAG will not run on a schedule, only manually
    start_date=datetime(2024, 11, 21),
    catchup=False,  # Do not backfill for past dates
) as dag:

    # Define the task
    hello_task = PythonOperator(
        task_id='hello_task',  # Task name
        python_callable=print_hello,  # Function to call
    )

# This DAG does not include dependencies or scheduling, so it only has one task.
