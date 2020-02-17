from DBConnector import DBConnector
import pandas as pd

def replace_vals_in_columns(df, cols, search_val=',', replace_val=''):
    for col in cols:
        df[col] = df[col].str.replace(search_val,replace_val)
    return df

def cols_astype(df, cols, new_type):
    for col in cols:
        df[col] = df[col].astype(new_type)
    return df


if __name__ == '__main__':
    ibex35 = pd.read_csv('data/csv/ibex_35.csv',sep=';')
    num_cols = ['CLOSING PRICE','OPEN','DAILY HIGH','DAILY LOW']
    ibex35 = replace_vals_in_columns(ibex35, num_cols)
    #ibex35 = cols_astype(ibex35, ['DATE'], 'datetime64[ns]')
    ibex35['DATE'] = pd.to_datetime(ibex35['DATE'], format='%m/%d/%Y')
    ibex35 = cols_astype(ibex35, num_cols, 'float64')
    ibex35['market_name'] = 'IBEX 35'
    ibex35.rename(columns={'DATE':'date_ref','OPEN':'open','CLOSING PRICE':'close','DAILY HIGH':'high','DAILY LOW':'low'}, inplace=True)
    ibex35 = ibex35[['market_name','date_ref','open','close','high','low']]
    print(ibex35.info())
    print(ibex35.tail())
    conn = DBConnector('connection/credentials.txt')
    for index,row in ibex35.iterrows():
        vals = '%s,' * len(ibex35.columns)
        conn.insert_values('Market',ibex35.columns, vals[:-1],list(row))
