from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.user_login, name='login'),
	path('logout/', views.user_logout, name='logout'),
	path('profile/<int:pk>/', views.profile, name='profile'),
	path('list/', views.list_user, name='list_user'),
]