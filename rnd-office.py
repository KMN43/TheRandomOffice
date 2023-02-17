import time
from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import random as rn

driver = webdriver.Chrome(executable_path=r"E:\Chromedriver\chromedriver_win32_chrome83\chromedriver.exe")
driver.get("https://giphy.com/search/theoffice")
urls = []
soup = BeautifulSoup(driver.page_source, "html.parser")

for attr in ['src']:
    tags = soup.select(f"[{attr}]")
    ls_links = []
    for tag in tags:
        ls = tag.attrs[attr]
        ls_links.append(ls)

def get_gif (lst):
    return list(filter(lambda x: "https://media" in x,lst))

f_links = get_gif(ls_links)

n = rn.randint(0,(len(f_links)-1))

gif = f_links[n]
