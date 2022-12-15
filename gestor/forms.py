from django import forms
from .models import Task, Usuarios

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un titulo'}),
            'description' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripcion'}),
            'important' : forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }

#class UsuariosForm(forms.ModelForm):
 #   class Meta:
  #      model = Usuarios
   #     field = ['username', 'password', ]
    #    widgets = {
     #       'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe usuario'}),
      #      'password' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe Contrasena'}),
       #     }
        