from django.conf.urls import include, url
from representation.views import auth, views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/', auth.url_view(), name='auth'),
]
