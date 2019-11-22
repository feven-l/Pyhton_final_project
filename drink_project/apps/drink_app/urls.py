from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main"),
<<<<<<< HEAD
    url(r'^infopage$', views.infopage),
    url(r'^search$', views.search),
    url(r'^search=(?P<search_term>\w+)$', views.search_results),
    url(r'^drinks/all', views.all_drinks)
=======
    url(r'^infopage/(?P<id>\d+)$', views.infopage, name="infopage"),
    url(r'^suggest$', views.suggest, name="suggest"),
    url(r'^alldrinks$', views.alldrinks, name="alldrinks")
>>>>>>> d23e6a5aa2c5d24b7f1ccdbc1d80f73f90741f45

]
