# python-csv-postgreSQL-NOC

Process of downloading a csv file and ingest to a postgreSQL instance with Docker Containers.

1) Installation of database using docker-compose. Need to have docker as sudo user and docker-compose installed

```bash
    cd database
    docker-compose up 
```

### Documents:

***pandas_to_postgreSQL.ipynb*** the python notebook has all the necesary steps to ingest the NOC information to a DB. the database has to be previously deploy with a Docker Container. 


the tables has been created in this way. for the insertion we will use pyodbc and insert from the two files

```sql

create table NOC_GROUP(
    GROUP_CODE varchar, 
    GROUP_TITLE varchar, 
    GROUP_DEFINITION varchar, 
);

create table NOC_MAJOR(
    GROUP_CODE varchar, 
    MAJOR_CODE varchar, 
    MAJOR_TITLE varchar, 
    MAJOR_DEFINITION varchar, 
);

create table NOC_MINOR(
    MAJOR_CODE varchar, 
    MINOR_CODE varchar, 
    MINOR_TITLE varchar, 
    MINOR_DEFINITION varchar, 
);

create table NOC_UNIT(
    MINOR_CODE varchar, 
    UNIT_CODE varchar, 
    UNIT_TITLE varchar, 
    UNIT_DEFINITION varchar, 
);

create table NOC_UNIT_EXAMPLE(
    UNIT_CODE varchar, 
    UNIT_EXAMPLE varchar, 
);


create table NOC_UNIT_INCLUSION(
    UNIT_CODE varchar, 
    UNIT_INCLUSION varchar, 
);

create table NOC_UNIT_EXCLUSION(
    UNIT_CODE varchar, 
    UNIT_EXCLUSION varchar, 
);

create table NOC_UNIT_MAIN_DUTIES(
    UNIT_CODE varchar, 
    UNIT_MAIN_DUTIES varchar, 
);

create table NOC_UNIT_EMPLOYMENT_REQUIREMENTS(
    UNIT_CODE varchar, 
    UNIT_EMPLOYMENT_REQUIREMENTS varchar, 
);

create table NOC_UNIT_ADITIONAL_INFORMATION(
    UNIT_CODE varchar, 
    UNIT_ADITIONAL_INFORMATION varchar, 
);

```