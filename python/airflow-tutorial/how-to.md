## How To

1. Set up and activate .venv

2. Indicate the airflow home directory. To make that the project directory (instead of root): 
```bash
export AIRFLOW_HOME=/Users/finlayoneill/code/airflow_tutorial
```

2. Navigate to the Airflow GitHub page and copy the pip install command. Note: I changed the `--contraint` flag param to reflect the version of python (ie. 3.11): 
```bash
AIRFLOW_VERSION=2.8.4

# Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
# See above for supported versions.
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"

CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example this would install 2.8.4 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.8.4/constraints-3.8.txt

python -m pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
```


4. Initialise the database (creates sqlite db) and set up a user: 
```bash
airflow db migrate

airflow users create \
    --username admin \
    --firstname Finlay \
    --lastname ONeill \
    --role Admin \
    --email fploneill@gmail.com

```

5. Start the airflow webserver (8080 is the default port):  
```bash
airflow webserver --port 8080
```

6. Start the scheduler in a separate terminal: 
```bash
export AIRFLOW_HOME=/Users/finlayoneill/code/airflow_tutorial
airflow scheduler
```

## References
- https://www.youtube.com/watch?v=K9AnJ9_ZAXE&t=2114s
- https://airflow.apache.org/docs/apache-airflow/stable/start.html