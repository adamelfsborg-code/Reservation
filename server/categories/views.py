from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from django.http import JsonResponse
import json 
import bcrypt
from .utils import *
# Create your views here.

class GetAllCategories(APIView):
    def get(self, request, format=None):
        id = request.GET.get(id)
    
        g = GetAllCategories()
        getAllCategories = g.get(id)

        if getAllCategories != '404':
            return JsonResponse({'msg': getAllCategories}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'categories not found'}, status=status.HTTP_404_NOT_FOUND)

class PinCategory(APIView):
    def post(self, request, format=None):
        kwargs = {
            'user_id': request.data.get('user_id'),
            'category_id': request.data.get('category_id')
        }

        p = PinCategory()
        pinCategory = p.post(**kwargs)

        if pinCategory != '400':
            return JsonResponse({'msg': 'category pinned'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'category not pinned'}, status=status.HTTP_400_BAD_REQUEST)

class DeletePinnedCategory(APIView):
    def delete(self, request, format=None):
        id = request.data.get('user_id')

        d = DeletePinnedCategory()
        deletePinnedCategory = d.delete(id)

        if deletePinnedCategory != '400':
            return JsonResponse({'msg': 'category unpinned'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'pinned not unpinned'}, status=status.HTTP_400_BAD_REQUEST)

