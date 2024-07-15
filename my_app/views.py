from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

# 앱요청
class HelloView( APIView ):

    def get( self, request ):
        return Response( { "message" : "Hello, world" } )
        pass # def get 끝

    pass # class HelloView 끝