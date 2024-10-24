# Churn Predictore 

## Description
    - A machine learning model using python which predicts whether a customer will churn (leave the company) or not.
    - **data.py`**: Handles data preprocessing and extraction.
    - **`model.py`**: Manages model training.
    - **`churn-prediction.ipynb`**: EDA(Exploratory Data Analysis), Model selection, Hyperparameter Tuning.
    - **'Airflow Pipeline for data processing and model training simultanouesly'


## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.8.20**: Make sure you have Python 3.8.20 installed on your machine.

## Installation Steps

1. **Install Python 3.8.20**
   - Download the installer from the official Python website: [Python Downloads](https://www.python.org/downloads/release/python-3820/).
   - Follow the installation instructions for your operating system.
   - Make sure to add Python to your system's PATH during installation.

2. **Clone the Repository**
   ```bash
   git clone https://github.com/apking2000/ChurnPredictor.git
   cd ChurnPredictor

3. **Install Required packages**
    - ****Create a virtual environment (optional but recommended)****:
        - python -m venv venv
        - source venv/bin/activate  # On macOS/Linux
        - .\venv\Scripts\activate   # On Windows
     - ****Install the required packages using the requirements file****:
        - pip install -r requirements.txt (bash terminal command)

## Airflow Installation

1. **Install Apache Airflow**
   - If Apache Airflow is already included in your `requirements.txt`, you can skip this step. Otherwise:

     - **Installing Apache Airflow**
       - Install Apache Airflow with the appropriate version constraints:
         ```bash
         pip install "apache-airflow[celery]==2.10.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.2/constraints-3.8.txt"
         ```

---

## Airflow Setup

1. **Initialize the Airflow Database**
   - Airflow uses a database to manage metadata. Initialize it:
     ```bash
     airflow db init
     ```

2. **Create an Admin User**
   - To access the Airflow web interface, create an admin user:
     ```bash
     airflow users create \
         --username admin \
         --password admin_password \
         --firstname FirstName \
         --lastname LastName \
         --role Admin \
         --email admin@example.com
     ```

---

## Running Airflow

1. **Temporary Set up location of dag in your current directory** 
    ```bash
    export AIRFLOW__CORE__DAGS_FOLDER=$(pwd)/dags
    ```
2. **Start the Airflow Web Server**
   - Start the web server on port 8080 to access the Airflow UI:
     ```bash
     airflow webserver --port 8080
     ```

3. **Start the Airflow Scheduler**
   - The scheduler is responsible for executing tasks:
     ```bash
     airflow scheduler
     ```
   - Once the web server is running, access the UI at `http://localhost:8080`.

4. **Trigger the DAG**
   - Go to the Airflow UI at `http://localhost:8080`.
   - Locate `run_two_scripts` in the list of DAGs.
   - Click the "Play" button to trigger the DAG manually.


