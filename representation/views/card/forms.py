from django.core.exceptions import ValidationError
from django.forms import ModelForm
from representation.models import BankCard


class BankCardForm(ModelForm):
    class Meta:
        model = BankCard
        fields = '__all__'

    def clean_number(self):
        data = self.cleaned_data['number']
        if len(data) < 16:
            raise ValidationError("Number %s is not validate" % data)
        return data
