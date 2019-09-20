from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('home',views.home,name='home'),
	path('all',views.all,name='all'),
	path('menuSelection',views.menuSelection,name='menuSelection'),
	path('newTodo',views.newTodo,name='newTodo'),
	path('viewTodo/<int:pk>/',views.viewTodo,name='viewTodo')
]