from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.logins, name='login'),
    path('logout', views.log_out, name='logout'),
    path('list', views.post_list, name='post_list'),
    path('pro', views.pro_list, name='pro_list'),
    path('pro/new/', views.pro_new, name='pro_new'),
    path('pro/edit/', views.pro_edit, name='pro_edit'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),    
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]

