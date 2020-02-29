import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
    Given a cursor and a connection object, iterates over pre-defined queries in `copy_table_queries` to transform data from provided S3 bucket to a set of staging tables
    
    Args:
        cur - a database cursor
        conn - a database connection object
    
    Returns:
        None
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Given a cursor and a connection object, iterates over pre-defined queries in `insert_table_queries` to transform data from a set of staging tables to a pre-defined STAR schema.
    
    Args:
        cur - a database cursor
        conn - a database connection object
    
    Returns:
        None
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Establishes a connection to Redshift using `dwh.cfg` config file. Transfroms raw data into a set of Redshift staging tables and finally transforms data into a set of fact and dimension tables.
    
    Args:
        None
    
    Returns:
        None
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format( 
        config['DWH']['host'], config['DWH']['dwh_db'],config['DWH']['dwh_db_user'],
        config['DWH']['dwh_db_password'], config['DWH']['dwh_port']
    ))

    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()