from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Premium(models.Model):
    price_one_month = models.FloatField()
    price_half_year = models.FloatField()
    price_year = models.FloatField()


class Tranzakcja(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    type_of_premium = models.IntegerField(default=1)
    buying_date = models.DateTimeField(default=timezone.now)
