from django.urls import path

from . import views


urlpatterns = [
    path('',views.homePage,name='home1'),
    path('About1/',views.AboutPage, name='About1'),
    path('Contact1/',views.ContactPage, name='Contact1')
]