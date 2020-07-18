from django.urls import path
from . import views

urlpatterns = [
	# path('', views.index, name='home'),
	path('home/', views.homePage, name='index'),
	path('news/', views.newsPage, name='news'),
	path('', views.playPage, name='play'),
	path('profile/', views.profilePage, name='profile'),
]
