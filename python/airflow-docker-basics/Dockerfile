FROM apache/airflow:2.8.4
ADD /wd_data_pipeline-0.0.1-py3-none-any.whl /wd_data_pipeline-0.0.1-py3-none-any.whl
# ADD requirements.txt .
RUN pip install /wd_data_pipeline-0.0.1-py3-none-any.whl
RUN pip install apache-airflow==${AIRFLOW_VERSION}

# Start with a Python 3.11 base image
# FROM python:3.11-slim

# # Set environment variables
# ENV AIRFLOW_HOME=/opt/airflow
# ENV AIRFLOW_VERSION=2.8.4
# ENV PYTHON_VERSION=3.11

# # Create airflow user
# RUN useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow

# # Install Apache Airflow with constraints to ensure compatibility
# # Note: As of my last update, there may not be official constraints for Python 3.11. You might need to adjust or remove the constraints.
# ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# RUN pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# # Copy your custom package and requirements
# COPY wd_data_pipeline-0.0.1-py3-none-any.whl ${AIRFLOW_HOME}/wd_data_pipeline-0.0.1-py3-none-any.whl
# # COPY requirements.txt ${AIRFLOW_HOME}/requirements.txt

# # Install your custom package and any additional requirements
# RUN pip install ${AIRFLOW_HOME}/wd_data_pipeline-0.0.1-py3-none-any.whl
# # RUN pip install -r ${AIRFLOW_HOME}/requirements.txt

# # Switch to airflow user
# USER airflow

# # Set working directory
# WORKDIR ${AIRFLOW_HOME}

# # Copy the entrypoint script
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# # Set the entrypoint script
# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["airflow", "webserver"]