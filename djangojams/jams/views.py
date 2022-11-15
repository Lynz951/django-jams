from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.

