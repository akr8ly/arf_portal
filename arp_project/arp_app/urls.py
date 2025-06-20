from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('chapter5/', views.chapter5_view, name='chapter5'),
    path('login/', views.login_view, name='login'),

]