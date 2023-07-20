import requests
from bs4 import BeautifulSoup

#вывод одной валюты на заданный момент
class Currency:
    DOLLAR_Rub = 'https://www.google.com/search?q=rehc+ljkkfhf&oq=rehc+ljkkfhf&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgKGIAEMgkIAhAAGAoYgAQyCQgDEAAYChiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyCQgGEAAYChiABDIJCAcQABgKGIAEMgkICBAAGAoYgAQyCQgJEAAYChiABNIBCDE0MzVqMWo3qAIAsAIA&sourceid=chrome&ie=UTF-8'
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    current_converted_price = 0
    difference = 4

    def __int__(self):
        self.current_converted_price = float(self.get_currency_price().replace(',','.'))

    def get_currency_price(self):
        full_page = requests.get(self.DOLLAR_Rub, headers=self.headers)

        soup = BeautifulSoup(full_page.content, 'html.parser')

        convert = soup.findAll('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
        return convert[0].text


    def check_currency(self):
        currency = float(self.get_currency_price().replace(',','.'))
        print('USD (Доллар США):'+ str(currency))
        exit()
        "----------------------" #нужно доработать
        self.check_currency()

currency = Currency()
currency.check_currency()



