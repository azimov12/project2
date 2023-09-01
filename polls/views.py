from django.shortcuts import render, get_object_or_404
from .models import Noutbooks, Keyboard
from django.http import JsonResponse
from .serializers import NoutbookSerializer, KeyboardSerializer

# Create your views here.

def detail(request, noutbook_id):
    noutbook = get_object_or_404(Noutbooks, id = noutbook_id)
    noubook_data = NoutbookSerializer(noutbook)
    
    return JsonResponse(noubook_data.data, safe=False)

def all(request):
    noutbook = Noutbooks.objects.all()
    result = NoutbookSerializer(noutbook, many=True)
    
    return JsonResponse(result.data, safe=False)   


def detail2(request, keyboard_id):
    keyboards = get_object_or_404(Keyboard, id = keyboard_id)
    keyboard_data = KeyboardSerializer(keyboards)
    
    return JsonResponse(keyboard_data.data, safe=False)

def all2(request):
    keyboards = Keyboard.objects.all()
    result = KeyboardSerializer(keyboards, many=True)
    
    return JsonResponse(result.data, safe=False)      