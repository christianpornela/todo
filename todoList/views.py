from django.shortcuts import render
import static
def home(request):
	return render(request,'todo/home.html')