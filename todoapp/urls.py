
from django.urls import path
from .views import *

urlpatterns = [

    path('', todo_list, name='todo_list'),
    path('create/', todo_create, name = 'todo_create'),
    path('<id>/', todo_detail, name = 'todo_detail'),
    path('<id>/update/', todo_update, name = 'todo_update'),
    path('<id>/delete/', todo_delete, name = 'todo_delete'),

]