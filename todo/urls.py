from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('tasks/', TaskList.as_view(), name='tasks'),
    path('tasksall/', TaskListall.as_view(), name='tasksall'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/create/', TaskCreate.as_view(), name='task-create'),
    path('task/update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task/delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
