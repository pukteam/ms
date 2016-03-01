from django.conf.urls import url
from representation.views import auth, views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/', auth.url_view()),
    url(r'^card/add$', views.add_new_bank_card, name='add'),
    url(r'^card/delete$', views.delete_bank_card, name='delete'),
    url(r'^investor$', views.investor, name='investor'),
    url(r'^investor/add$', views.add_new_investor, name='addinvestor'),
    url(r'^investor/delete$', views.delete_investor, name='deleteinvestor'),
]
