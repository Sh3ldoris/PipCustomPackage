import requests


class _RandomRequestsKeywords:

    def random_get_request(self):
        result = requests.get(url="https://api.coindesk.com/v1/bpi/currentprice.json")
        return result.json()
