from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from django.http import JsonResponse
import json 
import bcrypt
from .utils import *

class GetRestaurantsByCategory:
    def get(self, request, format=None):
        id = request.GET.get('id')

        g = GetRestaurantsByCategory()
        getRestaurantsByCategory = g.get(id)

        if getRestaurantsByCategory != '404':
            return JsonResponse({'msg': getRestaurantsByCategory}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'Restaurants not found'}, status=status.HTTP_404_NOT_FOUND)

class GetNearestRestaurants:
    def get(self, request, format=None):
        id = request.GET.get('id')

        g = GetNearestRestaurants()
        getNearestRestaurants = g.get(id)

        if getNearestRestaurants != '404':
            return JsonResponse({'msg': getNearestRestaurants}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'Restaurants not found'}, status=status.HTTP_404_NOT_FOUND)