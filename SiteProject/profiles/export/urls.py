from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	url(r'^xls/$', views.export_users_xls, name='export_users_xls'),
]
