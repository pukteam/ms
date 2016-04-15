# coding: utf-8
from django.contrib.auth.models import User
from django.db import models

operation_type = (
    ("WD", "Writing down"),
    ("R", "Refill"),
    ("O", "Other")
)


def write_down(card_id, sum):
    card = BankCard.objects.get(id=card_id)
    CardHistory(card=card, operation=0, balance_before=card.balance, balance_after=card.balance - sum).save()
    card.balance -= sum
    card.save()


def refill(card_id, sum):
    card = BankCard.objects.get(id=card_id)
    CardHistory(card=card, operation=1, balance_before=card.balance, balance_after=card.balance + sum).save()
    card.balance += sum
    card.save()


def money_transfer(from_card_id, to_card_id, sum):
    from_card = BankCard.objects.get(id=from_card_id)
    to_card = BankCard.objects.get(id=to_card_id)
    CardHistory(card=from_card, operation=2, balance_before=from_card.balance,
                balance_after=from_card.balance - sum).save()
    CardHistory(card=from_card, operation=2, balance_before=to_card.balance, balance_after=to_card.balance - sum).save()
    from_card.balance -= sum
    to_card.balance += sum
    from_card.save()
    to_card.save()


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

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            card = BankCard.objects.get(id=self.id)
            if card.balance < self.balance:
                CardHistory(card=card, operation="R", balance_before=card.balance, balance_after=self.balance).save()
            elif card.balance > self.balance:
                CardHistory(card=card, operation="WD", balance_before=card.balance, balance_after=self.balance).save()
            description = ""
            for item in BankCard().__dict__:
                if item not in ['_state', 'id', 'balance']:
                    if card.__dict__[item] != self.__dict__[item]:
                        description += "%s was changed from %s to %s" % (item, card.__dict__[item], self.__dict__[item])
            CardHistory(card=card, operation="O", balance_before=card.balance, balance_after=self.balance,
                        description=description).save()
        except:
            CardHistory(card=self, operation="O", balance_before=self.balance, balance_after=self.balance,
                        description="Card created").save()
        super(BankCard, self).save()

    def __unicode__(self):
        return "%s - %s" % (self.bank_name, self.number)


class Investor(models.Model):
    surname = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=50, blank=False)
    middle_name = models.CharField(max_length=50, blank=False)
    total = models.FloatField(max_length=100, null=False)

    def __unicode__(self):
        return "%s - %s" % (self.surname, self.total)


#
# class Operation(models.Model):
#     name = models.CharField(max_length=50)
#

class CardHistory(models.Model):
    card = models.ForeignKey('BankCard')
    # user = models.ForeignKey(User)
    operation = models.CharField(choices=operation_type, max_length=2)
    balance_before = models.FloatField(max_length=100)
    balance_after = models.FloatField(max_length=100)
    date_time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
