



# Data Warehouse

## Introduction
In this project a startup company called Sparkify is growing and its database needs are met only by moving to the cloud. The data engineering team is tasked with building an ETL pipeline that extracts information from JSON logs in S3 buckets and JSON metadata from their app and have it persisted to a PostgresSQL DB which is hosted on AWS Redshift.

## Datasets
Data is stored in public S3 buckets
Songs - Data is in a json format that contains information about the songs and artists
Events - Data is in a json format that contains information on user activity

## Schema 
![image](https://user-images.githubusercontent.com/72575271/110711316-576d6d00-81cd-11eb-82c8-fae78e5d6cfc.png)

There is one fact table(songplays) and four dimension tables(songs,users,artists and time)


## Project Files
1. create_tables.py - This script will create new tables and drop old tables when executed
2. etl.py - This script contains the logic that will load the staging tables and insert it into the tables created by the create_tables.py file.
3. dwh.cfg - Contains the redshift cluster information such as Host,DB name,DB User,DB Password,DB Port which is referenced by the etl.py file to connect to the redshift cluster
4. sql_queries.py - File that contains all the create, insert, delete SQL statements

## Steps to implement a database on Redshift
1.	Write out the CREATE/DROP SQL statements for each table in sql_queries.py
2.	Create a Redshift cluster and an IAM role  
3.	Input the necessary information(Host,DB name,DB User,DB Password,DB Port) in the dwh.cfg file which will allow us to input the variables into the create_tables.py so that we can connect to the postgres database
4.	The Copy logic must be written out so the S3 data is moved into a staging table on Redshift.
5.	Insert Queries must be written for each of the tables(must perform the necessary joins and transformation to some columns as needed to get the data in the right format)
6.	Run the etl.py and create_tables.py
7.	Try to query data and see if you get the expected results
8.	Delete the redshift cluster if queries return as expected

