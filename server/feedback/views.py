from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from django.http import JsonResponse
import json 
import bcrypt
from .utils import *

class CreateComment(APIView):
    def post(self, request, format=None):
        
        kwargs = {
            'user_id': request.data.get('id'),
            'restaurant_id': request.data.get('restaurant_id'),
            'comment': request.data.get('comment')
        }

        c = AddCommentToRestaurant()
        createComment = c.post(**kwargs)

        if createComment != '400':
            return JsonResponse({'msg': 'comment submited'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'comment not created'}, status=status.HTTP_400_BAD_REQUEST)

class CreateRating(APIView):
    def post(self, request, format=None):
        
        kwargs = {
            'user_id': request.data.get('user_id'),
            'restaurant_id': request.data.get('restaurant_id'),
            'rating': request.data.get('rating')
        }

        c = AddRatingToRestaurant(**kwargs)
        createRating = c.post(**kwargs)

        if createRating != '400':
            return JsonResponse({'msg': 'rating submited'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'rating not submited'}, status=status.HTTP_400_BAD_REQUEST)

class CreateReport(APIView):
    def post(self, request, format=None):
        
        kwargs = {
            'user_id': request.data.get('user_id'),
            'restaurant_id': request.data.get('restaurant_id'),
            'type_of_msg': request.data.get('type_of_msg'),
            'message': request.data.get('message')
        }

        c = SubmitReportToRestaurant()
        createReport = c.post(**kwargs)

        if createReport != '400':
            return JsonResponse({'msg': 'report submited'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'report not submited'}, status=status.HTTP_400_BAD_REQUEST)
class GetComment(APIView):
    def get(self, request, format=None):
        
        id = request.GET.get('id')

        c = GetAllCommentsForRestaurant()
        getComment = c.get(id)

        if getComment != '404':
            return JsonResponse({'msg': getComment}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'comments not found'}, status=status.HTTP_404_NOT_FOUND)


class GetAvgRating(APIView):
    def get(self, request, format=None):
        id = request.GET.get('id')

        c = GetAvgRatingForRestaurant()
        getAvgRating = c.get(id)

        if getAvgRating != '404':
            return JsonResponse({'msg': getAvgRating}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'comments not found'}, status=status.HTTP_404_NOT_FOUND)

