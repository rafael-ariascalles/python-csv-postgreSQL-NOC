# python-csv-postgreSQL-NOC

Process of downloading a csv file and ingest to a postgreSQL instance with Docker Containers.

1) Setup of the PostgreSQL Database, API with FastAPI and IDE with Jupyterlab/tensorflow using docker-compose. 
Need to have docker as sudo user and docker-compose installed

```bash
    docker-compose up 
```

2) In jupyter lab localhost:8888/lab Run necesary command for basic connection

```bash
    !pip install pandas
    !pip install sqlalchemy
    !pip install psycopg2-binary
```
3) Insert all the values needed for the Schema ingestion in PostgreSQL

```bash
    python noc_etl_process.py
```

### Documents:

***pandas_to_postgreSQL.ipynb*** the python notebook has all the necesary steps to ingest the NOC information to a DB. the database has to be previously deploy with a Docker Container. 


the tables has been created for a separation of topic a level of information. 

the list of table and primary keys are:

|table_name | primary key |
|---|---|
|noc_group|group_code|
|noc_major|major_code|
|noc_minor|minor_code|
|noc_unit|unit_code|
|noc_unit_example|unit_example_id|
|noc_unit_inclusion|unit_inclusion_id|
|noc_unit_exclusion|unit_exclusion_id|
|noc_unit_main_duties|unit_main_duties_id|
|noc_unit_employment_requirements|unit_employment_requirements_id|
|noc_unit_aditional_information|unit_aditional_information_id|
