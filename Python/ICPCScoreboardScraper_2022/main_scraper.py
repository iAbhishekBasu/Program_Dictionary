from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup
from datetime import datetime, timedelta

import time
import random
import json

from table_scraper import TableScraper

URL = 'https://codedrills.io/contests/icpc-india-2021-preliminary-online-round/scoreboard'


def sleepy(sleep_time: float = 0):
    if sleep_time:
        if random.choice(range(15)) == 0:  # so now there is a 1/15 chance of printing the statement
            print('Sleeping for {} secs'.format(sleep_time))
        time.sleep(sleep_time)
    else:
        print('Sleeping Infinitely')
        while 1:
            pass


def next_page(driver: webdriver.chrome.webdriver.WebDriver):
    nxt_page_ele = driver.find_element(by=By.XPATH,
                                       value='//*[@id="app"]/div/div[2]/main/div/span/span/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div[4]/button')
    nxt_page_ele.click()
    sleepy(5)


def func():
    with webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install())) as driver:
        driver.implicitly_wait(10)
        driver.get(url=URL)
        driver.maximize_window()
        data = {'header_data': None, 'rank_list': []}
        for _ in range((2174 - 25) // 25):
            table = driver.find_element(by=By.XPATH,
                                        value='//*[@id="app"]/div[1]/div[2]/main/div/span/span/div[2]/div/div/div[2]/div/div/div[2]/div[1]')
            table_innerHTML = (table.get_attribute('innerHTML'))
            scraper = TableScraper(table_innerHTML)
            response = scraper.scrape()
            if not data['header_data']:
                data['header_data'] = response['header_data']
            data['rank_list'].extend(response['body'])
            next_page(driver=driver)
    file_name = datetime.strftime(datetime.now(), '%Y%m%d_%H%M%S') + '.json'
    with open(file_name, 'w') as final_file:
        json.dump(data, final_file, indent=4)


def main():
    func()


if __name__ == '__main__':
    main()
