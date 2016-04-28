from django.contrib import admin
from import_export.admin import ExportMixin
from representation.models import BankCard, CardHistory, Investor, TestModel


class BaseResource(ExportMixin, admin.ModelAdmin):
    pass


class BankCardResource(BaseResource):
    pass


class InvestorResource(BaseResource):
    pass

admin.site.register(BankCard, BankCardResource)
admin.site.register(Investor, InvestorResource)
admin.site.register(CardHistory)
admin.site.register(TestModel)
