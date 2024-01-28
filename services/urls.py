from django.urls import path
from services.views import *

name='services'
urlpatterns = [
  path('', index, name='services')
]