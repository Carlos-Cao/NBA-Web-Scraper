from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

regularPpg = "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&Season=2019-20&SeasonType=Regular%20Season"
playoffsPpg = "https://stats.nba.com/players/traditional/?sort=PTS&dir=-1&SeasonType=Playoffs"
regularAst = "https://stats.nba.com/players/traditional/?sort=AST&dir=-1&SeasonType=Regular%20Season&Season=2019-20"
playoffsAst = "https://stats.nba.com/players/traditional/?sort=AST&dir=-1&SeasonType=Playoffs&Season=2019-20"
regularRpg = "https://stats.nba.com/players/traditional/?sort=REB&dir=-1&SeasonType=Regular%20Season&Season=2019-20"
playoffsRpg = "https://stats.nba.com/players/traditional/?sort=REB&dir=-1&SeasonType=Playoffs&Season=2019-20"

driver = webdriver.Chrome(ChromeDriverManager().install())


def RSppg():
    driver.get(regularPpg)
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


def POppg():
    driver.get(playoffsPpg)
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


def RSapg():
    driver.get(regularAst)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div/div[2]/div/div/button').click()

    time.sleep(5)
    players = driver.find_elements_by_class_name("player")
    assists = driver.find_elements_by_class_name("sorted")

    players_list = []
    assists_list = []

    for p in players:
        players_list.append(p.text)

    for at in assists[1:]:
        assists_list.append(at.text)

    for x, y in zip(players_list, assists_list):
        print(x + " - " + y + " apg")


def POapg():
    driver.get(playoffsAst)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div/div[2]/div/div/button').click()

    time.sleep(5)
    players = driver.find_elements_by_class_name("player")
    assists = driver.find_elements_by_class_name("sorted")

    players_list = []
    assists_list = []

    for p in players:
        players_list.append(p.text)

    for at in assists[1:]:
        assists_list.append(at.text)

    for x, y in zip(players_list, assists_list):
        print(x + " - " + y + " apg")


def RSrbg():
    driver.get(regularRpg)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div/div[2]/div/div/button').click()

    time.sleep(5)
    players = driver.find_elements_by_class_name("player")
    rebounds = driver.find_elements_by_class_name("sorted")

    players_list = []
    rebounds_list = []

    for p in players:
        players_list.append(p.text)

    for rb in rebounds[1:]:
        rebounds_list.append(rb.text)

    for x, y in zip(players_list, rebounds_list):
        print(x + " - " + y + " rpg")


def POrbg():
    driver.get(playoffsRpg)
    time.sleep(3)
    driver.find_element_by_xpath(
        '/html/body/div[3]/div[3]/div/div/div[2]/div/div/button').click()

    time.sleep(5)
    players = driver.find_elements_by_class_name("player")
    rebounds = driver.find_elements_by_class_name("sorted")

    players_list = []
    rebounds_list = []

    for p in players:
        players_list.append(p.text)

    for rb in rebounds[1:]:
        rebounds_list.append(rb.text)

    for x, y in zip(players_list, rebounds_list):
        print(x + " - " + y + " rpg")


POrbg()
