from django.urls import path
from .views import All, Detail, All2, Detail2, CreateKeyboardView,CreateNoutbookView, DeleteKeyboard, DeleteNoutbook, UpdateKeyboard, UpdateNoutbook

urlpatterns = [
    path('detail/<int:pk>/', Detail.as_view()),
    path('all/', All.as_view()),
    path('detail2/<int:pk>', Detail2.as_view()),
    path('all2/', All2.as_view()),
    path('create1/', CreateNoutbookView.as_view()),
    path('create2/', CreateKeyboardView.as_view()),
    path('update/<int:pk>', UpdateNoutbook.as_view()),
    path('update2/<int:pk>', UpdateKeyboard.as_view()),
    path('delete/<int:pk>', DeleteNoutbook.as_view()),
    path('delete/<int:pk>', DeleteKeyboard.as_view()),
]