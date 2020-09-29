# python-csv-postgreSQL-NOC

Process of downloading a csv file and ingest to a postgreSQL instance with Docker Containers.

### Documents:

***pandas_to_postgreSQL.ipynb*** the python notebook has all the necesary steps to ingest the NOC information to a DB. the database has to be previously deploy with a Docker Container. 


for the tables we will have

noc_tier_one

|group_code|title|description|
|---|---|---|

noc_tier_two
|group_code |major_code|title|description|
|---|---|---|---|

noc_tier_three
|major_code| minor_code| title| description|
|---|---|---|---|

noc_tier_four
|minor_code|unit_code|title|description|
|---|---|---|---|

noc_example

|unit_code|description|
|---|---|

