from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

from representation.models import BankCard


@login_required(login_url=reverse_lazy('representation:auth:login'))
def index(request):
    context = dict()
    if 'search' in request.GET and request.GET['search'] is not "":
        search = request.GET['search']
        context['search'] = search
        bank_cards = []
        _bank_cards = []
        for item in BankCard().__dict__:
            if item not in ['_state', 'id']:
                a = '%s__icontains' % item
                _bank_cards.append(BankCard.objects.filter(**{a: search}))
        for item in _bank_cards:
            bank_cards += item
        bank_cards = set(bank_cards)
    else:
        if request.user.is_superuser:
            bank_cards = BankCard.objects.filter(was_deleted=False)
        else:
            bank_cards = request.user.bankcard_set.filter(was_deleted=False)
    context['bank_cards'] = bank_cards
    return render(request, 'representation/index.html', context)


def set_lang(request):
    return render(request, 'representation/lang.html')
