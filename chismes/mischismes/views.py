from django.shortcuts import render
from rest_framework import generics
from .models import Chisme
from .serializers import ChismeSerializer


class ListChisme(generics.ListCreateAPIView):
    queryset = Chisme.objects.all()
    serializer_class = ChismeSerializer


class DetailChisme(generics.RetrieveUpdateDestroyAPIView):
    queryset = Chisme.objects.all()
    serializer_class = ChismeSerializer
