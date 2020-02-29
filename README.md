# AWS Data Warehouse and ETL for Sparkify

## Goal:
To transfer music streaming startup (`Sparkify`) data on available songs and user activity, to a database on an AWS cloud infrastructure. Define an ETL process with intermediate staging tables on Amazon Redshift PostgreSQL database. Define an efficient final STAR relational schema for the company. As well as provide `IaC` (Infrastructure as Code) for the company database cluster solution, and example queries.


## Code structure

- `dwh.cfg` : A configuration file. Provides details to:
    - `S3`: raw data bucket location
    - `IAM` : an `ARN` variable for the IAM role. (Filled automatically after following `IaC.ipynb`)
    - 'DWH' : defines details of the Redshift cluster readed by following `IaC.ipynb`. The `host` field will be filled automatically by runnin `IaC.ipynb`
- `IaC.ipynb`: a notebook to create a redshift cluster, verify its availability, create and attach IAM roles, check connections and delete existing cluster. Credentials for AWS user are typed in in a secure manner, and stored only in the session memory of the jupyter notebook.
- `sql_queries.py`: defines a set of queries for the staging and dimensional tables (create, drop and insert operations). 
- `create_tables.py`: connects to created Redshift cluster, drop any pre-existing tables and creates a blank STAR schema
- `etl.py`: copies data from S3 bucket into staging Reshift tables, and then populates the defined STAR schema


## STAR schema

### Fact Table
- `fact_songplay` - records in event data associated with song plays i.e. records with page NextSong
    - `songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent`

### Dimension Tables
- `dim_user` - users in the app
    - `user_id, first_name, last_name, gender, level`
- `dim_song` - songs in music database
    - `song_id, title, artist_id, year, duration`
- `dim_artist` - artists in music database
    - `artist_id, name, location, lattitude, longitude`
- `dim_time`- timestamps of records in songplays broken down into specific units
    - `start_time, hour, day, week, month, year, weekday` 


## How to run project


1. Launch a Redshift cluster with `IaC.ipynb` to create an instance, IAM roles, and to verify connection availability. 
2. Run `create_tables.py` to drop any pre-existing tables, and create a blank STAR schema for a given data model.
3. Run `etl.py` to stage data from AWS S3 bucket into Redshift and transfrom it into dimensional tables.
4. See `Example_queries.ipynb` for an easy way to connect to an existing database and execute example analytical queries.

5. (Optional) Go back to `IaC.ipynb` to delete created Redshift cluster