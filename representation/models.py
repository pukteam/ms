# coding: utf-8
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

operation_type = (
    ("WD", "Writing down"),
    ("R", "Refill"),
    ("O", "Other")
)


class BankCard(models.Model):
    number = models.CharField(max_length=16, unique=True)
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    balance = models.IntegerField()
    max_balance = models.IntegerField(default=10000)
    pin_code = models.CharField(max_length=4)
    availability = models.BooleanField(default=True)
    bank_name = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now=True)
    user_access = models.ManyToManyField(User)
    was_deleted = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            card = BankCard.objects.get(id=self.id)
            if card.balance < self.balance:
                CardHistory(card=card, operation="Refill", balance_before=card.balance,
                            balance_after=self.balance).save()
            elif card.balance > self.balance:
                CardHistory(card=card, operation="Writing down", balance_before=card.balance,
                            balance_after=self.balance).save()
            description = ""
            for item in BankCard().__dict__:
                if item not in ['_state', 'id', 'balance']:
                    if card.__dict__[item] != self.__dict__[item]:
                        description += "-%s was changed from %s to %s " % (
                        item, card.__dict__[item], self.__dict__[item])
            if description != "":
                CardHistory(card=card, operation="Other", balance_before=card.balance, balance_after=self.balance,
                            description=description).save()
            super(BankCard, self).save()
        except ObjectDoesNotExist:
            super(BankCard, self).save()
            CardHistory(card=self, operation="Other", balance_before=self.balance, balance_after=self.balance,
                        description="Card created").save()

    def __unicode__(self):
        return "%s - %s" % (self.bank_name, self.number)


class Investor(models.Model):
    surname = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    total = models.IntegerField()

    def __unicode__(self):
        return "%s - %s" % (self.surname, self.total)


class CardHistory(models.Model):
    card = models.ForeignKey('BankCard')
    operation = models.CharField(choices=operation_type, max_length=20)
    balance_before = models.IntegerField()
    balance_after = models.IntegerField()
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
