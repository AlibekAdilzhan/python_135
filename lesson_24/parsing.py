from itertools import product
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

service = Service(executable_path="C:\Program Files\Google\Chrome\chromedriver\chromedriver.exe")
browser = webdriver.Chrome(service=service)
url = ""
browser.get(url)
# soup = BeautifulSoup(browser.page_source)

with open("Iphone_prices.txt", "w", encoding="utf-8") as fo:
    for i in range(2, 7):
        page_source = browser.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        cards_info = soup.find_all("div", class_="item-card__info")
        for card in cards_info:
            info = card.find("a", class_="item-card__name-link")
            price = card.find("span", class_="item-card__prices-price")
            fo.write(f"{info.text},{price.text}\n")
        browser.get(url + f"?page={i}")
