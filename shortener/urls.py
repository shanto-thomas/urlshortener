# urls.py in the shortener app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/shorten/', views.shorten_url, name='shorten_url'),
    path('<str:short_url>/', views.redirect_to_original, name='redirect_to_original'),
]
