from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# Define default arguments
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'run_two_scripts',
    default_args=default_args,
    description='A simple DAG to run two Python scripts',
    schedule_interval='@daily',  # You can change this based on your needs
)

# Task to run the first Python script
run_script1 = BashOperator(
    task_id='run_script1',
    bash_command=f'python /Users/aakash.panda/Downloads/ChurnPredictor/dags/data.py',
    dag=dag,
)

# Task to run the second Python script
run_script2 = BashOperator(
    task_id='run_script2',
    bash_command=f'python /Users/aakash.panda/Downloads/ChurnPredictor/dags/model.py',
    dag=dag,
)

# Set task dependencies
run_script1 >> run_script2  # Script 2 will run after Script 1
