from django.conf.urls import url
from representation.views import auth, views, card, investor

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/', auth.url_view()),
    url(r'^card/', card.url_view()),
    url(r'^investor/', investor.url_view()),
]
