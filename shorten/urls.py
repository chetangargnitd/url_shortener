from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('home/', views.home, name="home"),
	path('shrink/', views.shrink, name="shrink"),
	path('<str:id>/', views.retrieve, name="retrieve"),
]