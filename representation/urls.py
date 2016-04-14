from django.conf.urls import url
from representation.views import auth, views, card

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/', auth.url_view()),
    url(r'^card/', card.url_view()),
    url(r'^investor$', views.investor, name='investor'),
    url(r'^investor/add$', views.add_new_investor, name='addinvestor'),
    url(r'^investor/edit/(?P<investor_id>\d+)$', views.edit_investor, name='editinvestor'),
    url(r'^investor/delete$', views.delete_investor, name='deleteinvestor'),
]
