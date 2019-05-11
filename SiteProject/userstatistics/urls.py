from django.urls import path, include


urlpatterns = [
	path('import/', include('userstatistics.import.urls')),
]
