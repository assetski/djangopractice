from django.shortcuts import render
from django.http import HttpResponse
from api.models import Task, TaskList
# Create your views here.
def index(request):
    return HttpResponse('<h1>Index works <h1>')

def task_list(request):
    tasks = TaskList.objects.all()
    resp = ""
    for task in tasks:
        resp+= '<p> {0} <p>'.format(task.name)
    return HttpResponse(resp)

def task_list_one(request, id):
    task = TaskList.objects.get(id = id)
    return HttpResponse('<h3> {0} <h3>'.format(task.name))

def task_one(request , id):
    task=Task.objects.get(id = id)
    resp = ""
    for task in tasks:
        resp += '<p> {0} <p>'.format(task.name)
    return HttpResponse(resp)

def task_list_one(request, id):
    task = TaskList.objects.get(id = id)
    return HttpResponse('<h3> {} <h3>'.format(task.name))

def task_one(request, id):
    task = Task.objects.get(id = id)
    return HttpResponse('<h3> {} {} {} {}<h3>'.format(task.name, task.created_at, task.due_on, task.status))

def list_task_one(request, id):
    tasks = TaskList.objects.get(id = id)
    all_tasks = Task.objects.all()
    str = ""
    for t in all_tasks:
        if (t.task_list.name == tasks.name):
            str += '<p> {} : {}  : {} <p>'.format(t.id, t.name, t.status)
    return HttpResponse(str)
