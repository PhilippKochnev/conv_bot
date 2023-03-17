
import requests
from config import exchanges
import json


class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, amount, sym):

        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f"Валюта {base} не найдена!")

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f"Валюта {sym} не найдена!")

        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={sym_key}&from={base_key}&amount={amount}"


        headers = {
            "apikey": "iSMFkwbpMRWnYNNlpONRJ6PqaK2ZVBwb"
        }

        response = requests.get(url, headers=headers)

        result = response.json()

        new_price = result['result']
        message = f" {base} = {amount}   {sym} = {new_price}"
        return message