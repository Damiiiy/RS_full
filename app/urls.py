from django.urls import path
from .views import *

urlpatterns = [
    path('reg/', register_bootcamp, name='register-bootcamp'),
    path('', index , name='home'),
]
