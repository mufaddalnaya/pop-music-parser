from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='search-home'),
    path('search', views.search),
]
