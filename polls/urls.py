from django.urls import path
from .views import All, Detail, All2, Detail2

urlpatterns = [
    path('detail/<int:noutbook_id>', Detail.as_view()),
    path('all/', All.as_view()),
    path('detail2/<int:keyboard_id>', Detail2.as_view()),
    path('all2/', All2.as_view()),
]