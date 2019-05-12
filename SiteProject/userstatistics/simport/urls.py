from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
	url(r'^xls/$', views.import_statistics_xls, name='import_statistics_xls'),
]
