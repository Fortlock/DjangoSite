from django.urls import path, include
from . import views
from django.conf.urls import url


urlpatterns = [
	path('', views.index, name='index'),
	path('export/', include('profiles.export.urls')),
]