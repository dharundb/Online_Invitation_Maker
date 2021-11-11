#map the urls with view functions

from django.contrib.admin.decorators import register
from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name='welcome'),
    path('login/',views.login_view,name='login'),
    path('signup/',views.signup,name='signup')
]
