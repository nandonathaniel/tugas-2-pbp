from django.urls import path
from todolist.views import register, login_user, logout_user, show_todolist, create_task, show_todolist_json, show_todolist_ajax, add_task_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist_ajax, name='show_todolist_ajax'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/',add_task_ajax, name = 'add_task_ajax'),
]