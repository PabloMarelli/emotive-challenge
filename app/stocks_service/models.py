from django.db import models
from django.contrib.auth.models import User

from take_home.models import CustomBaseModel

from stocks_service.utils import get_stock_price 



class UserProfile(CustomBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username


class Portfolio(CustomBaseModel):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.user.username}'s Portfolio"


class Stock(CustomBaseModel):
    ticker = models.CharField(max_length=10)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    portfolio = models.ForeignKey(Portfolio, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.ticker

    def get_price(self):
        print(f"Getting price for {self.ticker}")
        price = get_stock_price(self.ticker)
        return price

    def get_total_value(self, obj):
        return float(obj.quantity) * float(obj.price)

    def save(self, *args, **kwargs):
        self.price = self.get_price()[0]
        print(f"Price: {self.price}")
        super().save(*args, **kwargs)


class Recommendation(CustomBaseModel):
    ticker = models.CharField(max_length=10)
    
    def __str__(self):
        return self.ticker


