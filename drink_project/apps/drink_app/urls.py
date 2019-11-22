from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main"),
    url(r'^infopage/(?P<id>\d+)$', views.infopage, name="infopage"),
    url(r'^suggest$', views.suggest, name="suggest"),
    url(r'^alldrinks$', views.alldrinks, name="alldrinks")

]
