from django.urls import path
from . import views


urlpatterns = [
    path('', views.myIndex, name='inndex'),
]