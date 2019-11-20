from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^reg_process$', views.reg_process),
    url(r'^log_process$', views.log_process, name='login_id'),
    url(r'^logout$', views.logout)
]
