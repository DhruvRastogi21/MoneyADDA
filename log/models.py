# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from forex_python.converter import CurrencyRates
import pycountry
c=CurrencyRates()

list_of_currencies=['IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD',
                    'MXN', 'HUF', 'RON', 'MYR', 'SEK', 'SGD',
                    'HKD', 'AUD', 'CHF', 'KRW', 'CNY', 'TRY',
                    'HRK', 'NZD', 'THB', 'EUR', 'NOK', 'RUB',
                    'INR', 'JPY', 'CZK', 'BRL', 'PLN', 'PHP',
                    'ZAR','USD']

CURRENCY_CHOICES=[]
for currency in list(pycountry.currencies):
    if currency.alpha_3 in list_of_currencies:
        CURRENCY_CHOICES.append((currency.alpha_3,currency.name))
CURRENCY_CHOICES.sort(key=lambda x:x[1])
CURRENCY_CHOICES=tuple(CURRENCY_CHOICES)


class AccountHolder(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True)
    Acc_balance=models.DecimalField(default=0,decimal_places=2,max_digits=20)
    currency=models.CharField(max_length=100,choices=CURRENCY_CHOICES)

    def __str__(self):
        return self.user.username
    def debit(self,amount,currency):
        if currency == self.currency:
            self.Acc_balance -= amount
        else:
            self.Acc_balance -= c.convert(currency, self.currency, amount)
        self.save()
    def credit(self,amount,currency):
        if currency == self.currency:
            self.Acc_balance += amount
        else:
            self.Acc_balance += c.convert(currency, self.currency, amount)
        self.save()





class Transaction(models.Model):
    debited_from=models.ForeignKey(User,related_name='giver')
    username_of_recipient=models.ForeignKey(User,related_name='taker')
    amount=models.DecimalField(default=0,decimal_places=2,max_digits=20)
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES)
    date=models.DateField(null=True)






