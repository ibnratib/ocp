from django.urls import path
from .import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
# from django.conf.urls import handler404

# handler404= 'app.views.view404'
urlpatterns=[
    path('',views.acceuil,name='acceuil'),
    path('adm',views.adm,name='admin'),
    path('user',views.user,name='user'),
    path('deleteMail/<int:pk>/', views.deleteMail, name='deleteMail'),
    path('sendMail/<int:pk>/', views.sendMail, name='sendMail')

    ]
