from django.conf.urls import url
from representation.views import auth, views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/', auth.url_view(), name='auth'),
    url(r'^card/add$', views.add_new_bank_card, name='add'),
    url(r'^card/delete$', views.delete_bank_card, name='delete'),
]
