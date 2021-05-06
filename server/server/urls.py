from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('categories/', include('categories.urls')),
    path('feedback/', include('feedback.urls')),
    path('menus/', include('menus.urls')),
    path('reservation/', include('reservation.urls')),
    path('restaurants/', include('restaurants.urls')),
    path('tables/', include('tables.urls')),
    path('users/', include('users.urls'))
]
