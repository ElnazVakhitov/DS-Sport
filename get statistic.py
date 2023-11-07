import itertools
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

leagues = ['2015-2016', '2016-2017', '2017-2018', '2018-2019', '2019-2020', '2020-2021', '2021-2022']
for league in leagues:
    df_rating = pd.read_excel(io='Rating.xlsx', sheet_name=league)
    df = pd.read_csv(f"premier-league-{league}.csv")
    df = df.fillna(0)
    df['Дата'] = pd.to_datetime(df['Дата'], format='%d.%m.%Y %H:%M')

    team = "Арсенал"
    teams_stats = {}

    drename1 = dict([(stat, stat[3:]) for stat in df.columns])
    drename1["Дата"] = 'Дата'
    drename1["К1 Счет"] = 'Забито'
    drename1["К2 Счет"] = 'Пропущено'
    drename2 = dict([(stat, stat[3:]) for stat in df.columns])
    drename2["Дата"] = 'Дата'
    drename2["К1 Счет"] = 'Пропущено'
    drename2["К2 Счет"] = 'Забито'

    for team in df['Команда 1'].unique():
        team_stat1 = df.loc[(df["Команда 1"] == team)].loc[:,
                     df.columns.str.contains('(^К1)|(^К2 Счет)|(Дата)')].rename(
            drename1,
            axis=1)
        team_stat2 = df.loc[(df["Команда 2"] == team)].loc[:,
                     df.columns.str.contains('(^К2)|(^К1 Счет)|(Дата)')].rename(
            drename2,
            axis=1)
        team_stat_r = df_rating.loc[df_rating['Team'] == team].transpose().drop('Team')
        team_stat_r['Рейтинг'] = team_stat_r
        team_stat_r = team_stat_r['Рейтинг']
        teams_stats[team] = pd.concat(
            [pd.DataFrame(np.arange(1, 39), columns=['№ Game']),
             pd.concat([team_stat1, team_stat2]).sort_values(by=['Дата']).reset_index(drop=True)], axis=1)
        teams_stats[team] = pd.concat([teams_stats[team], team_stat_r], axis=1)

    team_prev_stat = teams_stats[team]

    data_for_learning = pd.DataFrame()

    for team in df['Команда 1'].unique():
        for i in range(17, 39):
            df_team = teams_stats[team].drop(['Дата', '№ Game'], axis=1)
            stat8_games = df_team[i - 8:i].agg(['min', 'max', 'mean', 'std', 'median'])
            dfl = {'Команда': team,
                   'Дата': teams_stats[team].iloc[i - 1]['Дата'],
                   '№ Game': i,
                   'Рейтинг': df_rating.loc[df_rating['Team'] == team][i].values[0]
                   }
            for name_stat, param_stat in itertools.product(stat8_games.columns, stat8_games.index):
                dfl[param_stat + ' ' + name_stat] = stat8_games[name_stat][param_stat]
            data_for_learning = data_for_learning.append(pd.DataFrame(data=[dfl.values()], columns=dfl.keys()))
    data_for_learning.to_csv(f'{league}.csv', index=False)
print('Done')
