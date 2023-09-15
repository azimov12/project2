from django.db import models

# Create your models here.
class Noutbooks(models.Model):
    noutbook_name = models.CharField(max_length=25, default='')
    noutbook_price = models.IntegerField()

class Keyboard(models.Model):
    k_brand_name = models.CharField(max_length=25, default='')
    k_price = models.IntegerField(default=0)