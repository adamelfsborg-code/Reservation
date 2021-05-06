from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from django.http import JsonResponse
import json 
import bcrypt
from .utils import *


class ReservateTable:
    def post(self, request, format=None):
        id = request.GET.get('id')
        user_id = request.GET.get('user_id')

        kwargs = {
            'id': id,
            'user_id': user_id,
        }
        c = ReservateTable()
        reservateTable = c.post(**kwargs)

        if reservateTable != '404':
            return JsonResponse({'msg': 'Table reservated'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'Table not reservated'}, status=status.HTTP_404_NOT_FOUND)
        
               