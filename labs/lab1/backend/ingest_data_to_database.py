from database import Database  # import database functions to open/close connections and execute queries
from constants import CLEANED_DATA_PATH, DATABASE_PATH  # import constants from constants.py

def ingest_csv_data_to_duckdb():
    """Ingests the cleaned CSV data into DuckDB."""
    translation_table = str.maketrans({"å": "a", "ä": "a", "ö": "o"})  # translation table for removing/replacing Swedish characters in schema names

    for directory_path in CLEANED_DATA_PATH.glob("*"): # iterate through all directories and files inside CLEANED_DATA_PATH
        schema_name = directory_path.name.lower().translate(translation_table) # schema name will be the folder name, with Swedish characters translated to replaced characters
        
        for csv_path in directory_path.glob("*"): # iteration to retrieve the table names 
            table_name = csv_path.name.lower().split(".")[0].translate(translation_table) # split the file name on "." to remove ".csv" and get only the table name at index [0], translating away Swedish characters

            with Database(DATABASE_PATH) as db: # using the database functions here to create database queries
                db.query(f"CREATE SCHEMA IF NOT EXISTS {schema_name};") # query to create the schema_name if it doesn't already exist
                db.query( # query to create the tables for the different schema names 
                    f"""
                        CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} AS 
                        SELECT * FROM read_csv_auto('{csv_path}');
                    """
                )

if __name__ == '__main__':
    ingest_csv_data_to_duckdb()
