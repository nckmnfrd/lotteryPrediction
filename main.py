from website_scraping import *

def group_data():
    df_lst = []
    for url in get_url():
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        date = get_data('td[class = "noBefore colour"]', soup)
        winning_nums = get_data('td[class = "noBefore nowrap"]', soup)
        winnings = get_data('td[class = "nowrap"]', soup)
        outcome = get_data('td[data-title = "Outcome"]', soup)

        df = create_df(date, winning_nums, winnings, outcome)
        df_lst.append(df)

    results = pd.concat(df_lst)
    return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    group_data().to_csv('lottery_winnings.csv', index = False)
