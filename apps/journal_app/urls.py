from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user$', views.register_user),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^morning_entry$', views.create_morning),
    # url(r'^books/add_book$', views.create_book),
    # url(r'^books/(?P<id>\d+)$', views.show_book),
    # url(r'^books/(?P<id>\d+)/create_review$', views.create_review),
    # url(r'^users/(?P<id>\d+)$', views.show_user),
    # url(r'^books/(?P<id>\d+)/delete_review$', views.delete_review),
    # url(r'^books$', views.books),
    url(r'^logout$', views.logout)
]