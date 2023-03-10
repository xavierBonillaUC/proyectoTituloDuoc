from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import  IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Usuarios

# Create your views here.
def home(request):
    return render(request, 'home.html') 

def signup(request):
    if request.method =='GET':
        return render(request, 'signup.html', {
        'form' : UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form' : UserCreationForm,
                    "error" : 'Username alredy exists'
                })
        return render(request, 'signup.html', {
            'form' : UserCreationForm,
            "error" : 'Password do not match'
        })
@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True) 
    return render(request, 'tasks.html', {'tasks' : tasks}) 

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted') 
    return render(request, 'task_completed.html', {'tasks' : tasks})     

@login_required
def create_task(request):

    if request.method == 'GET':
        return render(request, 'create_task.html' , {
            'form' : TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html' , {
            'form' : TaskForm,
            'error' : 'please provide valid data'
        })

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task': task, 'form': form,
            'error': "Error updating task"})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST' :
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST' :
        task.delete()
        return redirect('tasks')                            

@login_required
def signout(request):
    logout(request)
    return redirect('home')

#funcion para crear usuario
def signin(request):
    if request.method =='GET':
        return render(request, 'signin.html', {
        'form' : AuthenticationForm
         })
    else :
        Usuarios = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if Usuarios is None:
            return render(request, 'signin.html', {
                'form' : AuthenticationForm,
                'error' : 'Usuario o Contrase??a incorrecta '
            })
        else:
            login(request, Usuarios)
            if tipo_nivel == 'Funcionario':
                return render(request, 'f_home.html')
            elif tipo_nivel == 'Administrador':
                return render(request, 'a_home.html')
            else :    
                return render(request, 'd_home.html')
      


def create_internal_drives(request):
    return render(request, 'create_internal_drives.html') 

def d_home(request):
    return render(request, 'd_home.html') 

def d_crear(request):
    return render(request, 'd_crear.html') 

def d_admini(request):
    return render(request, 'd_admini.html') 

def d_ini(request):
    return render(request, 'd_ini.html') 


def a_home(request):
    return render(request, 'a_home.html')  

def a_crear(request):
    return render(request, 'a_crear.html')     

def a_adminus(request):
    return render(request, 'a_adminus.html')     

def a_crearuni(request):
    return render(request, 'a_crearuni.html')  

def a_adminuni(request):
    return render(request, 'a_adminuni.html') 

def a_adminrol(request):
    return render(request, 'a_adminrol.html') 

def a_crearrol(request):
    return render(request, 'a_crearrol.html') 

def a_admUni(request):
    return render(request, 'a_admUni.html') 

def a_crearrol(request):
    return render(request, 'a_crearrol.html') 

def f_home(request):
    return render(request, 'f_home.html')     

def f_crearTa(request):
    return render(request, 'f_crearTa.html')    

def f_tareasig (request):
    return render(request, 'f_tareasig.html') 

def f_vista (request):
    return render(request, 'f_vista.html') 

def f_carga (request):
    return render(request, 'f_carga.html') 

    


    