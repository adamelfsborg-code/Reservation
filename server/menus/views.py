from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from django.http import JsonResponse
import json 
import bcrypt
from .utils import *

class CreateMenu(APIView):
    def post(self, request, format=None):

        kwargs = {
            'restaurant_id': request.data.get('restaurant_id'),
            'food': request.data.get('food'),
            'drink': request.data.get('drink')
        }

        c = CreateMenuForRestaurant()
        createMenu = c.post(**kwargs)

        if createMenu != '400':
            return JsonResponse({'msg': 'menu created'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'menu not created'}, status=status.HTTP_400_BAD_REQUEST)


class GetMenu(APIView):
    def get(self, request, format=None):
        id = request.GET.get('id')

        c = GetMenuForRestaurant()
        getMenu = c.get(id)

        if getMenu != '404':
            return JsonResponse({'msg': getMenu}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'menu not found'}, status=status.HTTP_404_NOT_FOUND)