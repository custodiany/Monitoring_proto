from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='sys_mon'),
    path('sdp/', views.sdp, name='sdp'),
    path('fdp/', views.fdp, name='fdp'),
    path('efs/', views.efs, name='efs'),
    path('etc/', views.etc, name='etc'),
    path('rcom/', views.rcom, name='rcom'),
    path('drf/', views.drf, name='drf'),
    path('sdr/', views.sdr, name='sdr'),
    path('app/', views.app, name='app'),
    path('nms/', views.nms, name='nms'),
    path('was/', views.was, name='was'),
    path('log/', views.log, name='log'),
    path('test/', views.test, name='test'),

]