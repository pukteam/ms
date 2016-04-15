from django.forms import ModelForm, ValidationError
from .models import BankCard, Investor


class AddNewInvestor(ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
