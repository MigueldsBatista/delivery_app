from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login as django_login
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role
from django.contrib import messages




# Create your views here.
def login(request):

    if request.method=='POST':
        usuario=request.POST.get('usuario')
        senha=request.POST.get('senha')

        user = authenticate(username=usuario, password=senha)
        if user:
            django_login(request, user)
            

    return render(request, 'index.html')

def cadastro(request):
    if request.method=='POST':
        usuario=request.POST.get('usuario')
        email=request.POST.get('email')
        senha=request.POST.get('senha')
        user_type=request.POST.get('user_type')

        if User.objects.filter(username=usuario).exists():
            messages.error(request, 'Ja existe um usuário com esse nome')
            return redirect('cadastro')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Ja existe um usuário com esse email')
            return redirect('cadastro')
        else:
            if user_type:
                user=User.objects.create_user(username=usuario, email=email, password=senha)
                user.save()
                assign_role(user, user_type)
                messages.success(request, 'Cadastrado realizado com sucesso')
                return redirect('login')
            else:
                messages.error(request, 'Selecione um tipo de usuário')
                return redirect('cadastro')
            
    return render(request, 'cadastro.html')