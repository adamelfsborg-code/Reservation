from django.urls import path
from .views import *

urlpatterns = [
    path('reservate-table', ReservateTable.as_view())
]
