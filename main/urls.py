from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('literature', views.literature, name='literature'),
    path('film', views.film, name='film'),
    path('maths', views.maths, name='maths'),
    path("add", views.toAdd, name='toAdd')
]
