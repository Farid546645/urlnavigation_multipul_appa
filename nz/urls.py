from nz.views import *
from django.urls import path
app_name='ravi'

urlpatterns=[

    path('manasa/',manasa,name='manasa'),
    path('faridh/',faridh,name='faridh')
]