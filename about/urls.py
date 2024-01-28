from django.urls import path
from about.views import *

name='about'
urlpatterns = [
  path('', index, name='about')
]