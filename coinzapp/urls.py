from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('edit-profile/', views.editProfile, name='edit-profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('basic-option/', views.basicOption, name='basic-option'),
    path('advanced-option/', views.advancedOption, name='advanced-option'),
    path('premium-option/', views.premiumOption, name='premium-option')
]