from rest_framework import serializers

from .models import (
    Stock,
    Portfolio,
)


class StockSerializer(serializers.ModelSerializer):
    total_value = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = [
            'id',
            'ticker',
            'portfolio',
            'quantity',
            'price',
            'total_value'
        ]
    
    def get_total_value(self, obj):
        return float(obj.quantity) * float(obj.price)
    

class PortfolioSerializer(serializers.ModelSerializer):
    total_portfolio_value = serializers.SerializerMethodField()
    stocks = StockSerializer(many=True, read_only=True, source='stock_set')

    class Meta:
        model = Portfolio
        fields = [
            'id',
            'name',
            'owner',
            'total_portfolio_value',
            'stocks'
        ]

    def get_total_portfolio_value(self, obj):
        total_value = 0
        for stock in obj.stock_set.filter(portfolio=obj.id):
            total_value += stock.get_total_value(stock)
        return total_value






