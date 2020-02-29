import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Drops all tables defined in the variable `drop_table_queries` if they exist.
    
    Args:
        cur - a database cursor
        conn - a database connection object
        
    Returns:
        None
    """
    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates all tables defined in the variable `create_table_queries` if they exist.
    
    Args:
        cur - a database cursor
        conn - a database connection object
        
    Returns:
        None
    """
    
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
"""
    Establishes a connection to the Redshift cluster, drops any existing tables, and creates an empty set of staging, dimensional and fact tables.
    
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

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()