from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from todoList.models import ToDo
from .serializers import ToDoSerializer

@api_view(['GET','DELETE','PUT'])
def get_delete_update_todo(request,pk):
	try:
		todo=ToDo.objects.get(pk=pk)
	except ToDo.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)
		
	if request.method == 'GET':
		serializer=ToDoSerializer(todo)
		return Response(serializer.data)
	elif request.method == 'DELETE':
		todo.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	elif request.method == 'PUT':
		serializer=ToDoSerializer(todo,data=request.data,partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
@api_view(['GET','POST'])
def get_post_todo(request):
	if request.method == 'GET':
		todos=ToDo.objects.all()
		serializer=ToDoSerializer(todos,many=True)
		return (Response(serializer.data))
	if request.method == 'POST':
		serializer=ToDoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)