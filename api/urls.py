from django.urls import path,include
from api.views import index, task_list, task_list_one, list_task_one, task_one

urlpatterns = [
    path('',index),
    path('task_lists/',task_list),
    path('task_lists/<int:id>/', task_list_one),
    path('task_list/<int:id>/tasks/', list_task_one),
    path('tasks/<int:id>', task_one)
]