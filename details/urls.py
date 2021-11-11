from django.contrib.admin.decorators import register
from django.urls import path
from . import views

urlpatterns=[
    path('',views.occ,name='occasion'),
    path('wed',views.cred_wed,name='wed'),
    path('gather',views.cred_gather,name='gather'),
    path('bday',views.cred_bday,name='bday'),
    path('tempw',views.temp_wed,name='tempw'),
    path('tempg',views.temp_gath,name='tempg'),
    path('tempb',views.temp_bday,name='tempb'),
    path('wedstyle',views.wedstyling,name='wedstyle'),
    path('gathstyle',views.gathstyling,name='gathstyle'),
    path('bdaystyle',views.bdaystyling,name='bdaystyle'),
    path('edit',views.edit,name='edit'),
    path('mailshare',views.mailshare,name='mailshare'),
    path('logout/',views.logout_view,name='logout')
]
