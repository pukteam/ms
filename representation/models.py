# coding: utf-8
from django.db import models


class BankCard(models.Model):
    number = models.CharField(max_length=16, null=False, unique=True)
    surname = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, null=False)
    balance = models.FloatField(max_length=100, null=False)
    pin_code = models.CharField(max_length=4, null=False, blank=False)
    availability = models.BooleanField(null=False, default=True)
    bank_name = models.CharField(max_length=100, blank=False)

    def __unicode__(self):
        return "%s - %s" % (self.bank_name, self.number)
