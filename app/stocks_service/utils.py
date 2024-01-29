import requests
import logging
from random import randint

from django.conf import settings


logging=logging.getLogger('stocks_service')



def get_stock_price(ticker):

    API_KEY = settings.POLYGON_API_KEY
    url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            price = float(data['results'][0]['c'])
            return price, response
        elif response.status_code == 404:
            logging.error(f"Ticker {ticker} not found")
            return None, None
        elif response.status_code == 500:
            logging.error(f"Internal server error")
            return None, None
        else:
            logging.error(f"Error fetching data from Polygon.io {response.json()}")
            return None, None

    except requests.exceptions.RequestException as e:
        logging.error(f"Request exception: {e}")
        return None, None

used_indexes = []

def pick_random_recommendation():
    from stocks_service.models import Recommendation

    count = Recommendation.objects.count()

    # Reset the list if all indexes have been used
    if len(used_indexes) >= count:
        used_indexes.clear()

    if count > 0:
        random_index = randint(0, count - 1)

        # Keep picking a new random index if it's already been used
        while random_index in used_indexes:
            random_index = randint(0, count - 1)

        used_indexes.append(random_index)
        random_item = Recommendation.objects.all()[random_index]

        return random_item
    else:
        return None


def get_recommendation_data(ticker):
    API_KEY = settings.POLYGON_API_KEY
    url = f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={API_KEY}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['results'] 
            return data
        elif response.status_code == 404:
            logging.error(f"Ticker {ticker} not found")
            return None, None
        elif response.status_code == 500:
            logging.error(f"Internal server error")
            return None, None
        else:
            logging.error(f"Error fetching data from Polygon.io {response.json()}")
            return None, None

    except requests.exceptions.RequestException as e:
        logging.error(f"Request exception: {e}")
        return None, None



