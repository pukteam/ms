from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout

from django.shortcuts import redirect, render


def url_view():
    from django.conf.urls import url, include

    urlpatterns = [
        url(r'^login/$', _login, name='login'),
        url(r'^logout/$', _logout, name='logout'),
    ]

    return include(urlpatterns, namespace='auth')


def _login(request):
    if request.method == 'GET':
        return render(request, 'representation/login.html')
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)

    return redirect(reverse("representation:index"))


def _logout(request):
    logout(request)
    return redirect(reverse("representation:index"))

