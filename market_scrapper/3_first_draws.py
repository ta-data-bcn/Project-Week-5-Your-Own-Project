import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from DBConnector import DBConnector
import numpy as np
import itertools
import os

def create_folder_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def set_nans(df, cols):
    for col in cols:
        df[col][df[f'{col} == -1']] = np.nan()
    return df

##################################

def get_full_DataFrame(init, end):
    conn = DBConnector('connection/credentials.txt')
    query = f'''SELECT * FROM Market WHERE date_ref > '{init}' AND date_ref < '{end}' '''
    df = conn.read_sql(query)
    df.replace(-1, np.nan, inplace=True)
    return df

def get_single_DataFrame(init, end):
    conn = DBConnector('connection/credentials.txt')
    query = f'''SELECT * FROM Market WHERE date_ref > '{init}' AND date_ref < '{end}' AND market_name = 'IBEX_35' '''
    df = conn.read_sql(query)
    df.replace(-1, np.nan, inplace=True)
    return df


def get_Europe_DataFrame(init, end):
    conn = DBConnector('connection/credentials.txt')
    query = f'''SELECT * FROM Market WHERE date_ref > '{init}' AND date_ref < '{end}'
            AND market_name in ('IBEX_35','BEL_20','DAX','AEX','EURO_STOXX_50','SMI','CAC_40','FTSE_ITALIA','FTSE_100') '''
    df = conn.read_sql(query)
    df.replace(-1, np.nan, inplace=True)
    return df

def get_America_DataFrame(init, end):
    conn = DBConnector('connection/credentials.txt')
    query = f'''SELECT * FROM Market WHERE date_ref > '{init}' AND date_ref < '{end}'
            AND market_name in ('DOW_JONES','S&P_500','NASDAQ_100','S&P_TSX_60') '''
    df = conn.read_sql(query)
    df.replace(-1, np.nan, inplace=True)
    return df

def get_Asia_DataFrame(init, end):
    conn = DBConnector('connection/credentials.txt')
    query = f'''SELECT * FROM Market WHERE date_ref > '{init}' AND date_ref < '{end}'
            AND market_name in ('SHANGAI_COMPOSITE','NIKKEI_225','HANG_SHENG') '''
    df = conn.read_sql(query)
    df.replace(-1, np.nan, inplace=True)
    return df

##############################
##############################
##############################

def get_data(init, end):
    return get_Europe_DataFrame(init, end)

##############################
##############################
##############################

def df_to_benefits(init, end):
    df = get_data(init, end)
    df['diff'] = df.close - df.open
    markets = list(df.market_name.unique())
    benefits = {}
    for market in markets:
        total_diff = df.close.iloc[-1] - df.open.iloc[0]
        benefit = df.query(f'market_name == "{market}"')['diff'].sum() / total_diff
        benefits[market] = benefit
    return benefits

def graphs_by_date_range(init, end, name, id, shape, fsize):
    df = get_data(init, end)
    fig, ax = plt.subplots(shape[0], shape[1], figsize=fsize)
    market_names = list(df.market_name.unique())
    colors = iter(sns.color_palette('Set1', shape[0] * shape[1]))

    for i, ax in enumerate(ax.flat):
        if len(market_names) > i:
            market = market_names[i]
            data = df.query(f'market_name == "{market}"')
            c = next(colors)
            line = sns.lineplot(data.date_ref,data.close.interpolate(), color=c, markers=True, ax=ax)
            x_ax = [''] * len(data.date_ref)
            x_ax[0] = init
            x_ax[-1] = end
            line.set_xticklabels(x_ax)
            ax.set(xlabel=market)
    create_folder_if_not_exists(f'data/img/{id}/')
    plt.savefig(f'data/img/{id}/{name}.png', quality=100)

def medic_graphs(id, shape, fsize):
    ###################
    #### M E D I C ####
    ###################

    medics = []
    # listeriosis
    init = '2008-02-01'
    end = '2008-06-01'
    medics.append(df_to_benefits(init, end))
    init = '2008-01-01'
    end = '2008-06-01'
    graphs_by_date_range(init, end, f'1_{id}_listeriosis', id, shape, fsize)

    # influenza A virus
    init = '2009-05-01'
    end = '2010-9-01'
    medics.append(df_to_benefits(init, end))
    init = '2009-04-01'
    end = '2010-9-01'
    graphs_by_date_range(init, end, f'1_{id}_influenza', id, shape, fsize)

    # ebola Africa
    init = '2014-02-01'
    end = '2014-06-01'
    medics.append(df_to_benefits(init, end))
    init = '2014-01-01'
    end = '2014-06-01'
    graphs_by_date_range(init, end, f'1_{id}_ebola', id, shape, fsize)

    # coronavirus
    init = '2019-12-01'
    end = '2020-02-15'
    medics.append(df_to_benefits(init, end))
    init = '2019-11-01'
    end = '2020-02-15'
    graphs_by_date_range(init, end, f'1_{id}_corona', id, shape, fsize)

    df = pd.DataFrame(medics)
    print(df)
    corr = df.corr()
    f, ax = plt.subplots(figsize=fsize)
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5)
    create_folder_if_not_exists(f'data/img/{id}/')
    plt.savefig(f'data/img/{id}/corr_medic_{id}.png')

    sns.clustermap(df.corr(), center=0, cmap="vlag" ,linewidths=.75, figsize=(15, 15))
    plt.savefig(f'data/img/{id}/rel_medic_{id}.png')

def catphs_graphs(id, shape, fsize):
    #############################
    # C A T A S T R O P H E E S #
    #############################

    catphs = []
    # tsunami Tahiti
    init = '2010-01-01'
    end = '2010-06-01'
    graphs_by_date_range(init, end, f'2_{id}_tsunami_tahiti', id, shape, fsize)
    init = '2010-02-01'
    end = '2010-06-01'
    catphs.append(df_to_benefits(init, end))

    # tsunami Japan
    init = '2011-03-01'
    end = '2011-08-01'
    graphs_by_date_range(init, end, f'2_{id}_tsunami_japan', id, shape, fsize)
    init = '2011-04-01'
    end = '2011-08-01'
    catphs.append(df_to_benefits(init, end))

    # solar eruption
    init = '2012-03-01'
    end = '2012-09-01'
    graphs_by_date_range(init, end, f'2_{id}_solar_eruption', id, shape, fsize)
    init = '2012-04-01'
    end = '2012-09-01'
    catphs.append(df_to_benefits(init, end))

    # zika virus (Africa)
    init = '2015-11-01'
    end = '2016-03-01'
    graphs_by_date_range(init, end, f'2_{id}_zika', id, shape, fsize)
    init = '2015-12-01'
    end = '2016-03-01'
    catphs.append(df_to_benefits(init, end))

    df = pd.DataFrame(catphs)
    print(df)
    corr = df.corr()
    f, ax = plt.subplots(figsize=fsize)
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, cmap=cmap, vmax=.3, center=0, square=True, linewidths=.5)
    create_folder_if_not_exists(f'data/img/{id}/')
    plt.savefig(f'data/img/{id}/corr_catphs_{id}.png')

    sns.clustermap(df.corr(), center=0, cmap="vlag" ,linewidths=.75, figsize=(15, 15))
    plt.savefig(f'data/img/{id}/rel_catphs_{id}.png')



###################
##### M A I N #####
###################
# full shape, fsize = (4, 5), (30, 25)
# europe shape, fsize = (3, 3), (30, 25)
# america shape, fsize = (2, 2), (30, 25)
# asia shape, fsize = (1, 3), (30, 15)
# single shape, fsize(1, 1), (30, 15)
if __name__ == '__main__':
    shape, fsize = (3, 3), (30,25)
    place = 'europe'
    medic_graphs(place, shape, fsize)
    catphs_graphs(place, shape, fsize)