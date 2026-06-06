# Employee ETL Pipeline

## Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) data pipeline using Python, Pandas, PostgreSQL, and Apache Airflow.

The pipeline extracts employee data from a CSV file, performs data cleaning and transformation, and loads the processed data into a PostgreSQL database. The project also includes logging, error handling, environment variable management, incremental loading, containerization using Podman/Docker, and workflow orchestration using Apache Airflow.

## Tech Stack

* Python
* Pandas
* PostgreSQL
* SQLAlchemy
* Apache Airflow
* Podman/Docker
* Git & GitHub

## Features

* Extract employee data from CSV files
* Remove duplicate records
* Handle missing salary values
* Convert date columns into proper datetime format
* Load transformed data into PostgreSQL
* Incremental loading to avoid duplicate inserts
* Logging for monitoring ETL execution
* Error handling and exception tracking
* Environment variable configuration using `.env`
* Airflow DAG integration
* Containerized deployment using Podman

## Project Structure

employee-etl-pipeline/

├── data/

├── logs/

├── src/

│ ├── extract.py

│ ├── transform.py

│ ├── load.py

│ ├── config.py

│ ├── logger.py

│ └── main.py

├── dags/

│ └── employee_etl_dag.py

├── .env

├── requirements.txt

├── Dockerfile

└── README.md

## ETL Workflow

CSV File
↓
Extract
↓
Transform
↓
Incremental Load
↓
PostgreSQL
↓
Airflow Monitoring

## Future Enhancements

* Integration with Amazon S3 / MinIO
* Data validation framework
* Airflow task-level orchestration
* PySpark implementation
* Data warehouse integration
