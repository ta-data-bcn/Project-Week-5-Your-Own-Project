import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data/csv/S&P_500.csv')
    for index, row in df.iterrows():
        print(row)
