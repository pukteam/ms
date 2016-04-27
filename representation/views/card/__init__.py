from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from representation.models import BankCard
from .forms import BankCardForm
from representation.views.mixin import LoginRequiredMixin


def url_view():
    from django.conf.urls import url, include

    urlpatterns = [
        url(r'^add/$', BankCardAddFormView.as_view(), name='add'),
        url(r'^edit/(?P<card_id>\d+)/$', BankCardEditFormView.as_view(), name='edit'),
        url(r'^delete/$', delete_bank_card, name='delete'),
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
