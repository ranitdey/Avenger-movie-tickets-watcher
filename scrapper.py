#!/usr/bin/env python3
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import pymsgbox
import time
from selenium.webdriver.chrome.options import Options
from webhook_notifier import notify_webook
import os

# Note : if running on server, these environment variables are reqd : ZAPIER_WEBHOOK, CHROMEDRIVER_PATH, GOOGLE_CHROME_BIN, and TARGET_TITLE

def alert(message, running_on_server):
    if running_on_server:
        webhook_url = os.environ['ZAPIER_WEBHOOK']
        notify_webook(webhook_url, message)
    else:
        pymsgbox.alert(message, 'BookMyShow Notifier')


def movie_poller(running_on_server=False):
    print ("starting polling")

    if running_on_server:
        chrome_driver_path = os.environ['CHROMEDRIVER_PATH']
        options = webdriver.ChromeOptions()
        options.binary_location = os.environ['GOOGLE_CHROME_BIN']
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument("headless")
    else:
        chrome_driver_path = ChromeDriverManager().install()
        options = webdriver.ChromeOptions()
        options.add_argument("headless")

    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
    driver.get("https://in.bookmyshow.com/bengaluru")

    target_title = "Avengers: Endgame"
    if os.environ['TARGET_TITLE'] != '':
        target_title = os.environ['TARGET_TITLE']

    try:
        temp = driver.find_element(By.XPATH, "//*[@href='/movies']")
        temp.click()

    except WebDriverException:
        popup = driver.find_element(By.XPATH, "//*[@class='No thanks']")
        popup.click()
        temp = driver.find_element(By.XPATH, "//*[@href='/movies']")
        temp.click()

    time.sleep(10)
    sliders = driver.find_elements(By.XPATH, "//*[@class='showcase-card']/a")
    content = driver.find_elements(By.XPATH, "//*[@data-selector='movies']")

    list_of_movies = []
    for i in content:
        list_of_movies.append(i.get_attribute("data-title"))

    print ("Searching in \n")
    print (list_of_movies)

    if target_title in list_of_movies:
        alert("{} is here. Book your tickets now".format(target_title), running_on_server)

    else:
        print ("searching in \n")
        for j in sliders:
            print (j.get_attribute("href")[33:][:-11])
            if "Avengers" in j.get_attribute("href")[33:][:-11]:
                alert("{} is here. Book your tickets now".format(target_title), running_on_server)

    driver.close()

    if not running_on_server:
        print ("sleeping for 3 hours")
        time.sleep(10800)
        movie_poller()

movie_poller()
