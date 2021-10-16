from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Tutorial
from .serializers import TutorialSerializer
from rest_framework import generics

from tutorials import serializers


class TutorialListView(generics.ListAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class TutorialCreateView(generics.CreateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class TutorialDeleteView(generics.DestroyAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class TutorialUpdateView(generics.UpdateAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer


class TutorialDetailView(generics.RetrieveAPIView):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer
