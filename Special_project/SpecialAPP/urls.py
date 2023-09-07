from django.urls import path
from . import views

urlpatterns = [
    path('SpecialAPP/', views.Hello_word_fun, name='hello'),
]