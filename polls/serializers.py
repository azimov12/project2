from rest_framework import serializers
from .models import Noutbooks, Keyboard

class NoutbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noutbooks
        fields = ('noutbook_name', 'noutbook_price')

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = ('k_brand_name', 'k_price')       