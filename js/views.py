from django.shortcuts import render
import static
def home(request):
	return render(request,'home.html')
def all(request):
	return render(request,'all.html')
def menuSelection(request):
	return render(request,'menu.html')
def newTodo(request):
	return render(request,'newtodo.html')	
def viewTodo(request,pk):
	return render(request,'viewTodo.html')	