"""proccesapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gestor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('create_internal_drives/', views.create_internal_drives, name='create_internal_drives'),


    path('d_home/', views.d_home, name='d_home'),
    path('d_crear/', views.d_crear, name='d_crear'),
    path('d_admini/', views.d_admini, name='d_admini'),
    path('d_ini/', views.d_ini, name='d_ini'),

    path('a_home/', views.a_home, name='a_home'),
    path('a_crear/', views.a_crear, name='a_crear'),
    path('a_adminus/', views.a_adminus, name='a_adminus'),
    path('a_crearuni/', views.a_crearuni, name='a_crearuni'),
    path('a_adminuni/', views.a_adminuni, name='a_adminuni'),
    path('a_adminrol/', views.a_adminrol, name='a_adminrol'),
    path('a_admUni/', views.a_admUni, name='a_admUni'),
    path('a_crearrol/', views.a_crearrol, name='a_crearrol'),
    path('f_home/', views.f_home, name='f_home'),
    path('f_crearTa/', views.f_crearTa, name='f_crearTa'),
    path('f_tareasig/', views.f_tareasig , name='f_tareasig'),
    path('f_vista/', views.f_vista , name='f_vista'),
    path('f_carga/', views.f_carga , name='f_carga'),
    
    
    
    
    


    

]
