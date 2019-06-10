from django.db import models
from django.utils.timezone import now

class TaskList(models.Model):
    name = models.CharField(max_length=250)

class Task(models.Model):
    name = models.CharField(max_length=250)
    created_at= models.DateTimeField(default = now,blank = True)
    due_on=models.DateTimeField(default = now,blank = True)
    status=models.CharField(max_length=250)
    task_list=models.ForeignKey(TaskList, on_delete=models.DO_NOTHING)