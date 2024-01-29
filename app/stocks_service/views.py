from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from django.http import JsonResponse
import logging

from stocks_service.models import (
    Stock,
    Portfolio,
)
from stocks_service.serializers import (
    StockSerializer,
    PortfolioSerializer,
)
from stocks_service.utils import (
    get_recommendation_data,
    get_stock_price,
    pick_random_recommendation,
)

logging.getLogger('stocks_service')


@api_view(['GET'])
def get_stock_data(request, ticker):
    logging.info("fx: get_stock_data")

    price, response = get_stock_price(ticker)
    if response is None or price is None:
        logging.error(f"Error calculating price or no response")
        return JsonResponse({'error': 'Error calculating price or no response'}, status=500)

    if response.status_code == 200:
        formatted_response = {
            'ticker': ticker,
            'price': price,
        }
        return JsonResponse(formatted_response)
    else:
        logging.error(f"Error fetching data from Polygon.io {response.json()}")
        return JsonResponse({'error': 'Error fetching data from Polygon.io'}, status=response.status_code)


@api_view(['GET'])
def get_recommendation(request):

    random_item = pick_random_recommendation()

    if random_item is None:
        logging.error(f"No recommendations found")
        return JsonResponse({'error': 'No recommendations found, contact admin'}, status=500)

    ticker = random_item.ticker

    response_data = get_recommendation_data(ticker)

    try:
        stock_price = get_stock_price(ticker)[0]
    except Exception as e:
        logging.error(f"Error getting stock price: {e}")
        return JsonResponse({'error': f'Error getting stock price. Ticker: {ticker}'}, status=500)

    response = {
        "ticker": ticker,
        "name": response_data['name'],
        "price": stock_price,
        "description": response_data['description'],
        "market_cap": response_data['market_cap'],
        "primary_exchange": response_data['primary_exchange'],
        "list_date": response_data['list_date'],
        "locale": response_data['locale'],
        "homepage_url": response_data['homepage_url'],
    }
    return JsonResponse(response)


class StockList(generics.ListAPIView):
    """
    List portfolio stocks
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

class StockDetail(generics.RetrieveAPIView):
    """
    Portfolio stock CRUD
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

class StockCreate(generics.CreateAPIView):
    """
    Add stock to portfolio
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

class StockUpdate(generics.UpdateAPIView):
    """
    Update stock in portfolio
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)

class StockDelete(generics.DestroyAPIView):
    """
    Delete stock from portfolio
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = (IsAuthenticated,)



class PortfolioList(generics.ListAPIView):
    """
    List portfolio stocks
    """
    logging.info("fx: PortfolioList")

    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_profile = self.request.user.userprofile
        logging.info(f"User profile: {user_profile}")
        return Portfolio.objects.filter(owner=user_profile)

class PortfolioDetail(generics.RetrieveAPIView):
    """
    Portfolio stock CRUD
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (IsAuthenticated,)

class PortfolioCreate(generics.CreateAPIView):
    """
    Add stock to portfolio
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (IsAuthenticated,)

class PortfolioUpdate(generics.UpdateAPIView):
    """
    Update stock in portfolio
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (IsAuthenticated,)

class PortfolioDelete(generics.DestroyAPIView):
    """
    Delete stock from portfolio
    """
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (IsAuthenticated,)


