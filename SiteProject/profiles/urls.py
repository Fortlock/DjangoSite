from django.urls import path, include


urlpatterns = [
	path('export/', include('profiles.export.urls')),
]