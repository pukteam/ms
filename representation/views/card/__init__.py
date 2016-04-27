from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Sum
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, TemplateView

from representation.models import BankCard, CardHistory
from .forms import BankCardForm
from representation.views.mixin import LoginRequiredMixin, AdminRoleRequiredMixin


def url_view():
    from django.conf.urls import url, include

    urlpatterns = [
        url(r'^add/$', BankCardAddFormView.as_view(), name='add'),
        url(r'^edit/(?P<card_id>\d+)/$', BankCardEditFormView.as_view(), name='edit'),
        url(r'^delete/$', delete_bank_card, name='delete'),
        url(r'^blocked/$', BankCardBlocked.as_view(), name='blocked'),
        url(r'^total_balance/$', BankCardTotalBalance.as_view(), name='total_balance'),
    ]

    return include(urlpatterns, namespace='card')


class BaseBankCardView(LoginRequiredMixin):
    model = BankCard
    form_class = BankCardForm
    template_name = 'representation/addbankcard.html'

    def get_success_url(self):
        return reverse('representation:index')


class BankCardAddFormView(BaseBankCardView, CreateView):
    pass


class BankCardEditFormView(BaseBankCardView, UpdateView):
    def get_object(self, queryset=None):
        model = self.model.objects.filter(id=self.kwargs['card_id'], was_deleted=False)
        if model.first():
            return model.first()

    def get_context_data(self, **kwargs):
        context = super(BankCardEditFormView, self).get_context_data(**kwargs)

        context["card_history"] = CardHistory.objects.filter(card_id=self.kwargs['card_id'])
        return context


@login_required(login_url=reverse_lazy('representation:auth:login'))
def delete_bank_card(request):
    for item in request.POST:
        p = item.split("_", 1)
        if len(p) != 2:
            continue
        _card = BankCard.objects.get(id=p[1])
        _card.was_deleted = True
        _card.save(update_fields=['was_deleted'])
    return redirect(reverse('representation:index'))


class BankCardBlocked(TemplateView, AdminRoleRequiredMixin):
    template_name = 'representation/blocked_cards.html'

    def get_context_data(self, **kwargs):
        context = super(BankCardBlocked, self).get_context_data(**kwargs)

        context["blocked_cards"] = BankCard.objects.filter(availability=False)
        return context


class BankCardTotalBalance(TemplateView, AdminRoleRequiredMixin):
    template_name = 'representation/total_balance.html'

    def get_context_data(self, **kwargs):
        context = super(BankCardTotalBalance, self).get_context_data(**kwargs)
        bcb = BankCard.objects.filter(availability=False)\
            .aggregate(Sum('balance'))['balance__sum']
        ucb = BankCard.objects.filter(availability=True)\
            .aggregate(Sum('balance'))['balance__sum']
        context["blocked_cards_balance"] = bcb if bcb else -1
        context["unblocked_cards_balance"] = ucb if ucb else -1
        return context
