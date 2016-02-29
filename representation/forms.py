from django.forms import ModelForm, ValidationError
from .models import BankCard


class AddNewBankCard(ModelForm):
    class Meta:
        model = BankCard
        fields = [
            'number',
            'bank_name',
            'balance',
            'pin_code',
            'availability',
            'surname',
            'name',
            'middle_name',
        ]

    def clean_number(self):
        data = self.cleaned_data['number']
        if len(data) < 16:
            raise ValidationError("%s is not validate" % data)
        return data
