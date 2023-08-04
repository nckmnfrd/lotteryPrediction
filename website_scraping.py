import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_url():
    url1 = 'https://www.national-lottery.com/powerball/results/'
    url2 = '-archive'
    url_lst = []

    for i in range(1992, 2024):
        #print(url1 + str(i) + url2)
        url = url1 + str(i) + url2
        url_lst.append(url)
    return url_lst

def get_data(id, soup):
    lst = []
    for tag in soup.select(id):
        lst.append(tag.get_text(strip = True, separator= '\n'))
    return lst


def create_df(draw_date = None, results = None, jackpot = None, outcome = None):
    dic = {'draw_date': draw_date,
           'results': results,
           'jackpot': jackpot,
           'outcome': outcome}

    lot_df = pd.DataFrame(dic)
    lot_df = lot_df.replace(r'\n', ' ', regex = True)
    return lot_df
