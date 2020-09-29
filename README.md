# python-csv-postgreSQL-NOC

Process of downloading a csv file and ingest to a postgreSQL instance with Docker Containers.

1) Installation of database using docker-compose. Need to have docker as sudo user and docker-compose installed

```bash
    cd database
    docker-compose up 
```

### Documents:

***pandas_to_postgreSQL.ipynb*** the python notebook has all the necesary steps to ingest the NOC information to a DB. the database has to be previously deploy with a Docker Container. 


for the tables we will have

NOC_GROUP
|GROUP_CODE|GROUP_TITLE|GROUP_DESCRIPTION|
|---|---|---|

NOC_MAJOR
|GROUP_CODE|MAJOR_CODE|MAJOR_TITLE|MAJOR_DESCRIPTION|
|---|---|---|---|

NOC_MINOR
|MAJOR_CODE|MINOR_CODE|MINOR_TITLE|MINOR_DESCRIPTION|
|---|---|---|---|

NOC_UNIT
|MINOR_CODE|UNIT_CODE|UNIT_TITLE|UNIT_DESCRIPTION|
|---|---|---|---|

NOC_UNIT_EXAMPLE
|UNIT_CODE|UNIT_EXAMPLE|
|---|---|

NOC_UNIT_EXAMPLE
|UNIT_CODE|UNIT_EXAMPLE|
|---|---|
