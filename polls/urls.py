from django.urls import path
from .views import all, detail

urlpatterns = [
    path('detail/<int:noutbook_id>', detail),
    path('all/', all),
    path('detail2/<int:keyboard_id>', detail),
    path('all2/', all),
]