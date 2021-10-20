from django.db import models

# Create your models here.
class Todo(models.Model):

    title = models.CharField(max_length=250)
    due_date = models.DateField()
    completed = models.BooleanField()
    favourite = models.BooleanField()
    list = models.ForeignKey('TodoList',null=False,on_delete=models.CASCADE)

class TodoList(models.Model):
    name = models.CharField(max_length=250)
