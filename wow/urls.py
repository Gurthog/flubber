from django.urls import path

from . import views


app_name = 'wow'

urlpatterns = [
    path('', views.home, name="home"),
    path('bungle', views.bungle, name="bungle"),
]

