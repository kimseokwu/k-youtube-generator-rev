from typing import Optional
from selenium import webdriver

import utils.pipeline as pipeline

WEBDRIVER_PATH = './webdriver/chromedriver'

def get_driver(webdriver_path: str):
    driver = webdriver.Chrome(executable_path=webdriver_path)
    return driver

def extract(webdriver_path: Optional[str] = WEBDRIVER_PATH):
    driver = get_driver(webdriver_path)
    driver.get('https://www.youtube.com')


