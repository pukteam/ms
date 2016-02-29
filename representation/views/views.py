from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect

from representation.models import BankCard
from representation.forms import AddNewBankCard


@login_required(login_url=reverse_lazy('representation:auth:login'))
def index(request):
    bank_cards = BankCard.objects.all()
    context = dict(bank_cards=bank_cards)
    return render(request, 'representation/index.html', context)


@login_required(login_url=reverse_lazy('representation:auth:login'))
def add_new_bank_card(request):
    if request.method == 'GET':
        return render(request, 'representation/addbankcard.html', {
            'form': AddNewBankCard()
        })
    elif request.method == 'POST':
        print(request.POST)
        f = AddNewBankCard(request.POST)
        if f.is_valid():
            f.save()
            return redirect(reverse('representation:index'))
        else:
            return redirect(reverse('representation:add'), {'error': "test"})


@login_required(login_url=reverse_lazy('representation:auth:login'))
def delete_bank_card(request):
    t = {}
    for item in request.POST:
        p = item.split("_", 1)
        if len(p) != 2:
            continue
        k, v = p
        if k not in t:
            t[k] = []
        t[k].append(int(v))
    return redirect(reverse('representation:index'))
