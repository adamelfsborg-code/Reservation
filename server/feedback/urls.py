from django.urls import path
from .views import *


urlpatterns = [
    path('create-comment', CreateComment.as_view()),
    path('create-rating', CreateRating.as_view()),
    path('create-report', CreateReport.as_view()),
    path('get-comment-for-restaurant',GetComment.as_view()),
    path('get-rating-for-restaurant', GetAvgRating.as_view())
]