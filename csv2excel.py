import pandas as pd

# Reading the csv file
def csv2ex():
    dfs = []
    leagues = ['premier-league-2015-2016', 'premier-league-2016-2017', 'premier-league-2017-2018',
               'premier-league-2018-2019', 'premier-league-2019-2020', 'premier-league-2020-2021',
               'premier-league-2021-2022']
    for league in leagues:
        # df_rating = pd.read_excel(io='Rating.xlsx', sheet_name=league)
        df = pd.read_csv(f"{league}.csv")
        df = df.fillna(0)
        df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y %H:%M')
        df = df.sort_values(by='Дата')
        dfs.append(df[['Дата','Команда 1','Команда 2','К1 Счет','К2 Счет']])
    Eng = pd.concat(dfs)
    Eng.to_excel('Eng.xlsx')

def ex2csv():
    pd.read_excel('X.xlsx').to_csv('train.csv',index=True)
    pd.read_excel('y.xlsx').to_csv('test.csv',index=True)


csv2ex()
