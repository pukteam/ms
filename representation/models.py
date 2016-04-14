# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class BankCard(models.Model):
    number = models.CharField(max_length=16, unique=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    balance = models.FloatField(max_length=100)
    max_balance = models.FloatField(max_length=100, default=10000)
    pin_code = models.CharField(max_length=4)
    availability = models.BooleanField(default=True)
    bank_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    user_access = models.ManyToManyField(User)
    was_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return "%s - %s" % (self.bank_name, self.number)


class Investor(models.Model):
    surname = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, blank=False)
    total = models.FloatField(max_length=100, null=False)

    def __unicode__(self):
        return "%s - %s" % (self.surname, self.total)
