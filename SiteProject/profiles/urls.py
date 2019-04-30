from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	path('', views.index, name='index'),
	url(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]