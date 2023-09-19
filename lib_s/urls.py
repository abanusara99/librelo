from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),  # Include lib_m URLs for registration
    path('login/',views.login,name='login'),        # Include lib_m URLs for login
]
