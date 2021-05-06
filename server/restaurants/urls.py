from django.urls import path
from .views import *

urlpatterns = [
    path('get-restaurants-by-category', GetRestaurantsByCategory.as_view()),
    path('get-nearest-category', GetNearestRestaurants.as_view())
]
