from DBConnector import DBConnector
import pandas as pd
from os import listdir
from os.path import isfile, join
import sys

def replace_vals_in_columns(df, cols, search_val=',', replace_val=''):
    for col in cols:
        try:
            df[col] = df[col].str.replace(search_val,replace_val)
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert data to an integer.")
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
    return df

def cols_astype(df, cols, new_type):
    for col in cols:
        df[col] = df[col].astype(new_type)
    return df

def clear_nan(df, cols):
    for col in cols:
        df[col] = df[col][df[col].notnull()]
    return df


if __name__ == '__main__':
    csvpath = 'data/csv/'
    conn = DBConnector('connection/credentials.txt')
    for f in listdir(csvpath):
        filepath = join(csvpath, f)
        if not isfile(filepath):
            continue
        # continue only if is file and exists
        market = pd.read_csv(filepath,sep=';')
        num_cols = ['CLOSING PRICE','OPEN','DAILY HIGH','DAILY LOW']
        #market = replace_vals_in_columns(market, num_cols)
        # dates in python can't be translated into mysql dates
        # easy, fast and good option is to change date format to YYYY-MM-DD to be able to order them as str
        market = cols_astype(market, ['DATE'], 'datetime64[ns]')
        market = cols_astype(market, ['DATE'], 'str')
        market = cols_astype(market, num_cols, 'float64')
        market = clear_nan(market, num_cols)
        market['market_name'] = f[:-4]
        market.rename(columns={'DATE':'date_ref','OPEN':'open','CLOSING PRICE':'close','DAILY HIGH':'high','DAILY LOW':'low'}, inplace=True)
        market = market[['market_name','date_ref','open','close','high','low']]
        print(market.head())
        for index,row in market.iterrows():
            vals = '%s,' * len(market.columns)
            conn.insert_values('Market',','.join(market.columns), vals[:-1],list(row))
