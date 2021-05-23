
from django.urls import path, include

urlpatterns = [
    path('', include('dashboard.urls')),
    path('users/', include('users.urls')),
]
