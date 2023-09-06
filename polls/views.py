from django.shortcuts import render, get_object_or_404
from .models import Noutbooks, Keyboard
from django.http import JsonResponse
from .serializers import NoutbookSerializer, KeyboardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class Detail(APIView):
    def get(self, request, *args, **kwargs):
        noutbook = get_object_or_404(Noutbooks, id = kwargs['noutbook_id'])
        result = NoutbookSerializer(noutbook)
        return Response(result.data)

class All(APIView):    
    def get(self, request):
        noutbook = Noutbooks.objects.all()
        result = NoutbookSerializer(noutbook, many=True)
        
        return Response(result.data)   


class Detail2(APIView):
    def get(self, request, *args, **kwargs):
        keyboards = get_object_or_404(Keyboard, id = kwargs['keyboard_id'])
        keyboard_data = KeyboardSerializer(keyboards)

        return Response(keyboard_data.data)

class All2(APIView):
    def get(self, request):
        keyboards = Keyboard.objects.all()
        result = KeyboardSerializer(keyboards, many=True)

        return Response(result.data)   

class CreateNoutbookView(APIView):
    def post(self, request):
        user_body = request.data 
        serializer = NoutbookSerializer(data = user_body)          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    

class CreateKeyboardView(APIView):
    def post(self, request):
        user_body = request.data 
        serializer = KeyboardSerializer(data = user_body)          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)    