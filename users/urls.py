from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('feedback/view/', views.view_feedback, name='view_feedback')
]  