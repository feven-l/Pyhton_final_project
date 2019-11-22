from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main"),
    url(r'^infopage$', views.infopage),
    url(r'^search$', views.search),
    url(r'^search=(?P<search_term>\w+)$', views.search_results),
    url(r'^drinks/all', views.all_drinks)

]
