from rest_framework import serializers
from todoList.models import ToDo

class ToDoSerializer(serializers.ModelSerializer):

	class Meta:
		model = ToDo
		fields = ('id','title', 'notes', 'isStarred',
			'due_date', 'completed', 'created', 'category',
			'priority')