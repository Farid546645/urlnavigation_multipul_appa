from india.views import *
from django.urls import path
app_name='rohith'

urlpatterns=[
    path('virat/',virat,name='virat'),
    path('klrahul/',klrahul,name='klrahul'),

]