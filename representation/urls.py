from django.conf.urls import include, url
from representation.views import auth

urlpatterns = [
    url(r'^auth/', auth.url_view()),
]
