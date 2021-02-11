from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user$', views.register_user),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^morning_entry$', views.create_morning),
    url(r'^night_entry$', views.create_night),
    url(r'^days$', views.days),
    url(r'^days/(?P<id>\d+)/show$', views.show_day),
    url(r'^profile$', views.view_profile),
    url(r'^about$', views.about),
    url(r'^logout$', views.logout)
]