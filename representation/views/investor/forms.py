from django.forms import ModelForm
from representation.models import Investor


class InvestorForm(ModelForm):
    class Meta:
        model = Investor
        fields = '__all__'