from django.shortcuts import render, get_object_or_404
from .models import Noutbooks, Keyboard
from .serializers import NoutbookSerializer, KeyboardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics 
# Create your views here.

class Detail(generics.RetrieveAPIView):
    queryset = Noutbooks.objects.all()
    serializer_class = NoutbookSerializer 

class All(generics.ListAPIView):
    queryset = Noutbooks.objects.all()
    serializer_class = NoutbookSerializer 

class Detail2(generics.RetrieveAPIView):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

class All2(APIView):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer  

class CreateNoutbookView(generics.CreateAPIView):
    queryset = Noutbooks.objects.all()
    serializer_class = NoutbookSerializer 

class CreateKeyboardView(generics.CreateAPIView):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer

class DeleteNoutbook(generics.DestroyAPIView):   
    queryset = Noutbooks.objects.all()
    serializer_class = NoutbookSerializer    

class DeleteKeyboard(generics.DestroyAPIView):   
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer   

class UpdateNoutbook(generics.UpdateAPIView):   
    queryset = Noutbooks.objects.all()
    serializer_class = NoutbookSerializer    

class UpdateKeyboard(generics.UpdateAPIView):   
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer     