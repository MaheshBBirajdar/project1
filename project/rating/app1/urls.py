from django.urls import path
from .views import *

urlpatterns = [
   
    path('course/', Create, name='create'),
    path('rate/<int:id>/',add_review, name="rate_review"),
    
]
