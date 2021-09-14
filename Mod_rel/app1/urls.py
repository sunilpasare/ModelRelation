from django.urls import path
from .import views

urlpatterns=[

    path('log/',views.userlogin,name='login'),
    path('logo/',views.logoutview,name='logout'),
    path('register/',views.userregister,name='register')
]