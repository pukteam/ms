from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render


@login_required(login_url=reverse_lazy('representation:auth:login'))
def index(request):
    return render(request, 'representation/index.html')
