import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from todolist.models import Task
# Create your views here.

#Ga dipake dulu krn ada ajax
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    all_tasks = Task.objects.filter(user = request.user)
    context = {
        'list_tasks': all_tasks,
        'pemilik': request.user,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    context = {
        'pemilik': request.user,
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def show_todolist_json(request):
    all_tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", all_tasks), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist_ajax")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        judul = request.POST.get("title")
        desc = request.POST.get("description")
        Task.objects.create(user = request.user, date = timezone.now(), title = judul, description = desc)

        return redirect('todolist:show_todolist_ajax')

    context = {'pemilik' : request.user}
    return render(request, 'create-task.html', context)

@login_required(login_url='/todolist/login/')
def add_task_ajax(request):
    if request.method == 'POST':
        this_task = Task()
        this_task.user = request.user
        this_task.date = timezone.now()
        this_task.title = request.POST.get('title')
        this_task.description = request.POST.get('description')

        this_task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
