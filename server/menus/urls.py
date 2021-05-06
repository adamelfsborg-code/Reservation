from django.urls import path
from .views import *


urlpatterns = [
   path('create-menu', CreateMenu.as_view()),
   path('get-menu', GetMenu.as_view())
]