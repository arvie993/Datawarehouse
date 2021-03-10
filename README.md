



# Data Warehouse

## Introduction
In this project a startup company called Sparkify is growing and its database needs are met only by moving to the cloud. The data engineering team is tasked with building an ETL pipeline that extracts information from JSON logs in S3 and JSON metadata from their app and have it persisted to a PostgresSQL DB which is hosted on AWS Redshift.

## Schema 
![image](https://user-images.githubusercontent.com/72575271/110711316-576d6d00-81cd-11eb-82c8-fae78e5d6cfc.png)

There is one fact table(songplays) and four dimension tables(songs,users,artists and time)

## Steps to achieve result
1. Write out the CREATE/DROP SQL statements for each table in sql_queries.py
2. Create a Redshift cluster and an IAM role  
3. Input the necessary information(Host,DB name,DB User,DB Password,DB Port) in the dwh.cfg file which will allow us to input the variables into the create_tables.py so that we can connect to the postgres database
4.The Copy logic must be written out so the S3 data is moved into a staging table on Redshift.
5.Insert Queries must be written for each of the tables(must perform the necessary joins and transformation to some columns as needed to get the data in the right format)
6.Run the etl.py and create_tables.py
7.Try to query data and see if you get the expected results
8. Delete the redshift cluster if queries return as expected
