#!/usr/bin/env python3
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import pymsgbox
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium.webdriver.chrome.options import Options


def movie_poller():
    print ("starting polling")
    chrome_driver_path = ChromeDriverManager().install()
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path=chrome_driver_path, chrome_options=options)
    driver.get("https://in.bookmyshow.com/bengaluru")
    list_of_movies = []
    target_title = "Avengers: Endgame"
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

    for i in content:
        list_of_movies.append(i.get_attribute("data-title"))

    print ("Searching in \n")
    print (list_of_movies)


    if target_title not in list_of_movies:
        pymsgbox.alert(target_title + " is here. Book your tickets now", 'Title')
    print ("searching in \n")
    for j in sliders:
        print (j.get_attribute("href")[33:][:-11])
        if "Avengers" in j.get_attribute("href")[33:][:-11]:
            pymsgbox.alert(target_title + " is here. Book your tickets now", 'Title')

    driver.close()
    print ("sleeping for 3 hours")
    time.sleep(10800)
    movie_poller()

movie_poller()





