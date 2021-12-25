from .views import Home
from django.urls import path, include

urlpatterns = [
    path('', Home, name='home')
]
