from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('verify/<str:token>/', views.send_email_confirmation, name='verify_account'),
]
