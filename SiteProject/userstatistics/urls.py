from django.urls import path, include


urlpatterns = [
	path('import/', include('userstatistics.simport.urls')),
]
