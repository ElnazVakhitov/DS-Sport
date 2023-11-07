from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

PATH_CHROME = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
PATH_CHROME_DRIVER = 'C:\\Users\\elnaz\\Downloads\\chromedriver-win64-117\\chromedriver-win64\\chromedriver.exe'


def get_stat(driver, match):
    match.click()
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.LINK_TEXT, 'СТАТИСТИКА').click()
    [date, team1, score1, _, score2, _, team2] = driver.find_element(By.CLASS_NAME, "duelParticipant").text.split(
        '\n')
    all_match_stat = {
        "Дата": date,
        "Команда 1": team1,
        "Команда 2": team2,
        "К1 Счет": int(score1),
        "К2 Счет": int(score2)
    }
    sleep(0.5)
    for stat in driver.find_elements(By.CLASS_NAME, "stat__row"):
        [stat1, stat_name, stat2] = stat.text.split('\n')
        if stat1[-1] == '%':
            stat1, stat2 = stat1[:-1], stat2[:-1]
        all_match_stat["К1 " + stat_name] = int(stat1)
        all_match_stat["К2 " + stat_name] = int(stat2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    return all_match_stat


options = Options()
options.binary_location = PATH_CHROME
driver = webdriver.Chrome(executable_path=PATH_CHROME_DRIVER,
                          chrome_options=options)
leagues = ['premier-league-2022-2023']
for league in leagues:
    driver.get('https://www.flashscore.ru.com/football/england/' + league + '/results/')
    sleep(2)
    try:
        driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    except Exception as e:
        do = 0
    while 1:
        try:
            driver.find_element(By.CLASS_NAME, 'event__more').click()
        except StaleElementReferenceException:
            break
        except Exception as e:
            continue
    matches = driver.find_elements(By.CLASS_NAME, 'event__match')
    s = get_stat(driver, matches[0])
    df = pd.DataFrame(data=[s.values()], columns=s.keys())
    i = 0
    for match in matches[1:]:
        i += 1
        s = get_stat(driver, match)
        df = df.append(pd.DataFrame(data=[s.values()], columns=s.keys(), index=[i]))
    df.to_csv(league + '.csv', index=False),
driver.close()
