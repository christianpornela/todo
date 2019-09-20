from django.db import models
from django.contrib.auth.models import User
import datetime

class category(models.Model):
	categoryname=models.CharField(max_length=40)
	def __str__(self):
		return "{}".format(self.categoryname)

class priority(models.Model):
	priorityname=models.CharField(max_length=40)
	def __str__(self):
		return "{}".format(self.priorityname)
	
class ToDo(models.Model):
	title=models.CharField(max_length=40)
	notes=models.TextField()
	isStarred= models.BooleanField()
	due_date=models.DateField(default=datetime.date.today)
	created=models.DateTimeField(auto_now_add=True,editable=False)
	category=models.ForeignKey(category,on_delete=models.CASCADE)
	priority=models.ForeignKey(priority,on_delete=models.CASCADE)

	def __str__(self):
		return "{} - {}".format(self.title,self.category)