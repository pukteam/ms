from django.forms import ModelForm, ValidationError
from .models import BankCard, Investor


class AddNewBankCard(ModelForm):
    class Meta:
        model = BankCard
        fields = '__all__'

    def clean_number(self):
        data = self.cleaned_data['number']
        if len(data) < 16:
            raise ValidationError("Number %s is not validate" % data)
        return data


class AddNewInvestor(ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'
