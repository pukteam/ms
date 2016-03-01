from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect

from representation.models import BankCard, Investor
from representation.forms import AddNewBankCard, AddNewInvestor


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
        f = AddNewBankCard(request.POST)
        if f.is_valid():
            f.save()
            return redirect(reverse('representation:index'))
        else:
            return redirect(reverse('representation:add'))


@login_required(login_url=reverse_lazy('representation:auth:login'))
def delete_bank_card(request):
    for item in request.POST:
        p = item.split("_", 1)
        if len(p) != 2:
            continue
        BankCard.objects.get(id=p[1]).delete()
    return redirect(reverse('representation:index'))


def investor(request):
    context = dict(investors=Investor.objects.all())
    return render(request, 'representation/investor.html', context)


@login_required(login_url=reverse_lazy('representation:auth:login'))
def add_new_investor(request):
    if request.method == 'GET':
        return render(request, 'representation/addinvestor.html', {
            'form': AddNewInvestor()
        })
    elif request.method == 'POST':
        f = AddNewInvestor(request.POST)
        if f.is_valid():
            f.save()
            return redirect(reverse('representation:investor'))
        else:
            return redirect(reverse('representation:addinvenstor'))


@login_required(login_url=reverse_lazy('representation:auth:login'))
def delete_investor(request):
    for item in request.POST:
        p = item.split("_", 1)
        if len(p) != 2:
            continue
        Investor.objects.get(id=p[1]).delete()
    return redirect(reverse('representation:investor'))