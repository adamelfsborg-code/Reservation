from django.urls import path
from .views import *

urlpatterns = [
    path('create-table', CreateTable.as_view()),
]
