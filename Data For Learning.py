import pandas as pd

leagues = ['2015-2016', '2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022']
dfl = pd.DataFrame()
for league in leagues:
    df = pd.read_csv(f'premier-league-{league}.csv')
    df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y %H:%M')
    df_stat = pd.read_csv(f'{league}.csv')
    df_stat['Дата'] = pd.to_datetime(df_stat['Дата'])
    dfl_1 = df[['Дата', 'Команда 1', 'Команда 2']]
    dfl_1['Забито'] = df['К1 Счет']
    dfl_1['Пропущено'] = df['К2 Счет']
    dfl_1 = dfl_1.merge(df_stat, how='inner', left_on=['Дата', 'Команда 1'], right_on=['Дата', 'Команда'],
                        suffixes=('', '_1'))
    dfl_1 = dfl_1.merge(df_stat, how='inner', left_on=['Дата', 'Команда 2'], right_on=['Дата', 'Команда'],
                        suffixes=('', '_2'))
    dfl_1 = dfl_1.drop(['Команда 1', 'Команда 2'], axis=1)
    dfl_1 = pd.concat([dfl_1, pd.Series([1] * dfl_1.shape[0], name='Our field')], axis=1)
    dfl_2 = df[['Дата', 'Команда 1', 'Команда 2', 'К1 Счет', 'К2 Счет']]
    dfl_2['Забито'] = df['К2 Счет']
    dfl_2['Пропущено'] = df['К1 Счет']
    dfl_2 = dfl_2.merge(df_stat, how='inner', left_on=['Дата', 'Команда 2'], right_on=['Дата', 'Команда'],
                        suffixes=('', '_1'))
    dfl_2 = dfl_2.merge(df_stat, how='inner', left_on=['Дата', 'Команда 1'], right_on=['Дата', 'Команда'],
                        suffixes=('', '_2'))
    dfl_2 = dfl_2.drop(['Команда 1', 'Команда 2'], axis=1)
    dfl_2 = pd.concat([dfl_2, pd.Series([0] * dfl_2.shape[0], name='Our field')], axis=1)
    dfl = pd.concat([dfl, dfl_1, dfl_2], axis=0)
dfl.to_csv(f'data.csv', index=False)
print('Done')
