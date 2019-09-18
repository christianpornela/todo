from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path(
		'v1/todo/<int:pk>/',
		views.get_delete_update_todo,
		name='get_delete_update_todo'
	),
	path(
		'v1/todo/',
		views.get_post_todo,
		name='get_post_todo'
	)
]