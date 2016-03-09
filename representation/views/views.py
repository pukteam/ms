from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render, redirect

from representation.models import BankCard, Investor
from representation.forms import AddNewBankCard, AddNewInvestor


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
        bank_cards = BankCard.objects.all()
    context['bank_cards'] = bank_cards
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
            return render(request, 'representation/addbankcard.html', {
                'form': f
            })


@login_required(login_url=reverse_lazy('representation:auth:login'))
def edit_bank_card(request, card_id):
    _bank_card = BankCard.objects.get(id=card_id)
    if request.method == 'GET':
        return render(request, 'representation/addbankcard.html', {
            'form': AddNewBankCard(instance=_bank_card)
        })
    elif request.method == 'POST':
        f = AddNewBankCard(request.POST, instance=_bank_card)
        if f.is_valid():
            f.save()
            return redirect(reverse('representation:index'))
        else:
            return render(request, 'representation/addbankcard.html', {
                'form': f
            })


@login_required(login_url=reverse_lazy('representation:auth:login'))
def delete_bank_card(request):
    for item in request.POST:
        p = item.split("_", 1)
        if len(p) != 2:
            continue
        BankCard.objects.get(id=p[1]).delete()
    return redirect(reverse('representation:index'))


@login_required(login_url=reverse_lazy('representation:auth:login'))
def investor(request):
    context = dict()
    if 'search' in request.GET and request.GET['search'] is not "":
        search = request.GET['search']
        context['search'] = search
        investors = []
        _investors = []
        for item in Investor().__dict__:
            if item not in ['_state', 'id']:
                a = '%s__icontains' % item
                _investors.append(Investor.objects.filter(**{a: search}))
        for item in _investors:
            investors += item
        investors = set(investors)
    else:
        investors = Investor.objects.all()
    context['investors'] = investors
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
            return render(request, 'representation/addinvestor.html', dict(
                form=f
            ))


@login_required(login_url=reverse_lazy('representation:auth:login'))
def edit_investor(request, investor_id):
    _investor = Investor.objects.get(id=investor_id)
    if request.method == 'GET':
        return render(request, 'representation/addinvestor.html', {
            'form': AddNewInvestor(instance=_investor)
        })
    elif request.method == 'POST':
        f = AddNewInvestor(request.POST, instance=_investor)
        if f.is_valid():
            f.save()
            return redirect(reverse('representation:investor'))
        else:
            return render(request, 'representation/addinvestor.html',
                          dict(
                              form=f
                          ))


@login_required(login_url=reverse_lazy('representation:auth:login'))
def delete_investor(request):
    for item in request.POST:
        p = item.split("_", 1)
        if len(p) != 2:
            continue
        Investor.objects.get(id=p[1]).delete()
    return redirect(reverse('representation:investor'))
