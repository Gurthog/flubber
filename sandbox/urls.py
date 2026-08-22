from django.urls import path

from . import views


app_name = 'sandbox'


urlpatterns = [
    path('', views.home, name='home'),
    path('teleport', views.teleport, name='teleport'),

    # portals
    path('equidistant', views.equidistant, name='equidistant'),
    path('periodic', views.periodic, name='periodic'),
    path('squeeze', views.squeeze, name='squeeze'),
]

