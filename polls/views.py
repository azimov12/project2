from django.shortcuts import render, get_object_or_404
from .models import Noutbooks, Keyboard
from django.http import JsonResponse

# Create your views here.

def detail(request, noutbook_id):
    a = Noutbooks.objects.get_object_or_404(id=noutbook_id)
    data = {
        'noutbook_name': a.noutbook_name,
        'noutbook_price': a.noutbook_price
    }
    return JsonResponse(data, safe=False)

def all(request):
    result = []
    all_data = Noutbooks.objects.all()
    for ele in all_data:
        result.append({
            'noutbook_name': ele.noutbook_name,
            'noutbook_price': ele.noutbook_price
        })
    return JsonResponse(result, safe=False)   


def detail2(request, keyboard_id):
    a = Keyboard.objects.get_object_or_404(id=keyboard_id)
    data = {
        'brand_name': a.k_brand_name,
        'price': a.k_price
    }
    return JsonResponse(data, safe=False)

def all2(request):
    result = []
    all_data = Noutbooks.objects.all()
    for ele in all_data:
        result.append({
            'brand_name': ele.k_brand_name,
            'price': ele.k_price
        })
    return JsonResponse(result, safe=False)       