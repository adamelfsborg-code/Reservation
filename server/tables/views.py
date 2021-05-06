from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from django.http import JsonResponse
import json 
import bcrypt
from .utils import *


class CreateTable(APIView):
    def post(self, request, format=None):

        kwargs = {
            'restaurant_id': request.GET.get('restaurant_id'),
            'seats_quantity': request.GET.get('seats_quantity'),
            'table_nr': request.GET.get('table_nr')
        }

        c = CreateTable()

        createTable = c.post(**kwargs)

        if createTable != '404':
            return JsonResponse({'msg': 'Table created'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'Table not created'}, status=status.HTTP_404_NOT_FOUND)
        