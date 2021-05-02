from django.urls import path
from .views import *

urlpatterns = [
    path('get-all-categories', GetAllCategories.as_view()),
    path('pin-category', PinCategory.as_view()),
    path('delete-pinned-category', DeletePinnedCategory.as_view())
]
