from django.urls import path

from . import views


app_name = 'sandbox'


urlpatterns = [
    path('', views.home, name='home'),
    path('teleport', views.teleport, name='teleport'),

    # portals
    path('squeeze', views.squeeze, name='squeeze'),
]

