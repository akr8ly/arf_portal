from django.urls import path
from . import views

urlpatterns = [
     path('', views.home_view, name='home'),
    path('static-page/', views.static_page_view, name='static_page'),
    path('login/', views.login_view, name = 'login'),
    
]