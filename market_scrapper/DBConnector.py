import pymysql
from pathlib import Path
import sys
import pandas as pd

class DBConnector:
    """
    Class created to manage MySQL easier.

    Parameters:
    path (str): path to recover a file with the credentials
    """
    def __init__(self, path):
        """
        Constructor
        
        Parameters:
        path (str): relative or full path to the connection file
            structure of the file:
            - host
            - user
            - password
            - database
        """
        credentials = Path(path)
        # check file exists
        if (not credentials.exists()):
            print('ERROR - COULD NOT RECOVER CREDENTIAL FILES')
            sys.exit()
        # open credentials super secret file
        with open(credentials) as f:
            lines = f.read().splitlines()
            f.close()
        # create connector
        self.conn = pymysql.connect(host=lines[0], user=lines[1], password=lines[2], db=lines[3])
        # create cursor
        self.cursor = self.conn.cursor()
        self.insert_sql = 'INSERT INTO {} ({}) VALUES ({})'

    def read_sql(self, sql):
        """
        executes the given slq sentence. It can only execute SELECT sentences.
        
        Parameters:
        sql: the query to execute
        
        Returns:
        pandas.DataFrame with result
        """
        return pd.read_sql(sql, self.conn)

    def insert_values(self, table, columns, values, row):
        """
        insert given values to specified table

        Parameters:
        table: the table to insert values
        columns: columns affected, params to insert
        values: specify a string with '%s' for each param
            -- 3 parameters would be str('%s,%s,%s')
        row: array / tuple / list with values to insert in the
            order of the columns var
        """
        try:
            self.cursor.execute(self.insert_sql.format(table, columns, values), row)
            self.conn.commit()
        except pymysql.Error as e:
            if (str(e).__contains__('Duplicate')):
                print(f'DUPLICATED VALUE --> {row}')
            else:
                print(f'ERROR - could not insert querie {self.insert_sql.format(table, columns, values)} with params {row}')
            self.conn.rollback()

    def __del__(self):
        print('-----------------------')
        try:
            self.cursor.close()
            self.conn.close()
        except:
            print('could not close connection')
        finally:
            print('Connector destroyed.')
