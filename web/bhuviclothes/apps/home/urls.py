from django.urls import path, include
from apps.home import views


urlpatterns = [
    path('', views.Home, name='Home')
]
