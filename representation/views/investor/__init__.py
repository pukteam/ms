from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView

from representation.models import Investor
from .forms import InvestorForm


def url_view():
    from django.conf.urls import url, include

    urlpatterns = [
        url(r'^$', investor_all, name="root"),
        url(r'^add/$', InvestorAddFormView.as_view(), name='add'),
        url(r'^edit/(?P<investor_id>\d+)/$', InvestorEditFormView.as_view(), name='edit'),
        url(r'^delete/$', delete_investor, name='delete'),
    ]

    return include(urlpatterns, namespace='investor')


# todo refactor change function to class
@login_required(login_url=reverse_lazy('representation:auth:login'))
def investor_all(request):
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


class InvestorAddFormView(CreateView):
    model = Investor
    form_class = InvestorForm
    template_name = 'representation/addinvestor.html'

    def get_success_url(self):
        return reverse('representation:investor:root')


class InvestorEditFormView(UpdateView):
    model = Investor
    form_class = InvestorForm
    template_name = 'representation/addinvestor.html'

    def get_object(self, queryset=None):
        model = self.model.objects.filter(id=self.kwargs['investor_id'])
        if model.first():
            return model.first()

    def get_success_url(self):
        return reverse('representation:investor:root')


# todo refactor change function to class
@login_required(login_url=reverse_lazy('representation:auth:login'))
def delete_investor(request):
    for item in request.POST:
        p = item.split("_", 1)
        if len(p) != 2:
            continue
        Investor.objects.get(id=p[1]).delete()
    return redirect(reverse('representation:investor:root'))
