from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('counter', v.counter, name='counter'),
    path('register', v.register, name='register'),
]