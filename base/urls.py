from django.urls import path
from base.views import *

name='base'
urlpatterns = [
  path('', index, name='base')
]