from django.shortcuts import render,redirect
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from requests import Request, post
from django.http import JsonResponse
import json 
import bcrypt
from .utils import *

class RegisterUser(APIView):
    def post(self, request, format=None):
        """[try to add user column to user table in db]

        Args:
            request ([str]): [user data]
        Returns:
            [str]: [returns 200 if success else 400]
        """
        r = CreateUser()
        kwargs = {
            'full_name': request.data.get('full_name'),
            'email': request.data.get('email'),
            'phone_number': request.data.get('phone_number'),
            'password': self.hashPassword(request.data.get('password'))
        }
        checkEmailAndPhoneNumber = self.get(kwargs['email'],kwargs['phone_number'])
        if checkEmailAndPhoneNumber != '400':
            registerUser = r.post(**kwargs)
            if registerUser == '200':
                return JsonResponse({'msg': 'Account created'}, status=status.HTTP_200_OK)
            return JsonResponse({'msg': 'Could not create account'}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse({'msg': 'Email or Phone Number already exists'}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, email,phone_number):
        """[check if email or phone_number already exists in db]

        Args:
            email ([str]): [user-email]
            phone_number ([str]): [user-phone_number]

        Returns:
            [str]: [returns "email or phone_number already exists" if email or phone_number in db else 200]
        """
        r = CreateUser()
        return r.get(email,phone_number)

    def hashPassword(self, password):
        """[hash password]

        Args:
            password ([str]): [user-password]

        Returns:
            [type]: [returns the new hashed password]
        """
        return bcrypt.hashpw(password, bcrypt.gensalt())

class LoginUser(APIView):
    def put(self, request, format=None):
        """[login user by adding session token to user column in table]

        Args:
            request ([str]): [data]
        Returns:
            [str]: [token]
        """
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        kwargs = {
            'email': request.data.get('email'),
            'password': request.data.get('password'),
            'token': self.request.session.session_key
        }
        
        l = LoginUser()
        loginUser = l.get(**kwargs)
        if loginUser != '400':
            return JsonResponse({'msg': loginUser}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'user not found'}, status=status.HTTP_404_NOT_FOUND)


class LogoutUser(APIView):
    def put(self, request, format=None):
        """[try to logg out user by setting token to null in user column in table]

        Args:
            request ([str]): [data]

        Returns:
            [str]: ["logged out" if success else "user not found"]
        """
        id = request.GET.get('id')

        l = LogoutUser()
        logoutUser = l.put(id)

        if logoutUser != '400':
            return JsonResponse({'msg': 'logged out'}, status=status.HTTP_200_OK)
        return JsonResponse({'msg': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
