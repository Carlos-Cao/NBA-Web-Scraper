from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

playoffs = "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&SeasonType=Playoffs"

regular = "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&Season=2019-20&SeasonType=Regular%20Season"


#df = pd.DataFrame(columns=["Player", "Points"])
driver = webdriver.Chrome(ChromeDriverManager().install())


def regularSeason():
    driver.get(regular)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div/div[2]/div/div/button').click()

    time.sleep(5)
    players = driver.find_elements_by_class_name("player")
    points = driver.find_elements_by_class_name("sorted")

    players_list = []
    points_list = []

    for p in players:
        players_list.append(p.text)

    for pt in points[1:]:
        points_list.append(pt.text)

    for x, y in zip(players_list, points_list):
        print(x + " - " + y + " ppg")


def playoffsSeason():
    driver.get(playoffs)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div/div[2]/div/div/button').click()

    time.sleep(5)
    players = driver.find_elements_by_class_name("player")
    points = driver.find_elements_by_class_name("sorted")

    players_list = []
    points_list = []

    for p in players:
        players_list.append(p.text)

    for pt in points[1:]:
        points_list.append(pt.text)

    for x, y in zip(players_list, points_list):
        print(x + " - " + y + " ppg")


""" data_tuples = list(zip(players_list, points_list))
temp_df = pd.DataFrame(data_tuples, columns=["Player", "Points"])

df = df.append(temp_df)
 """


playoffsSeason()
