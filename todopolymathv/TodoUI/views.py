from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm


# Create your views here.

@login_required(login_url='todoui:loginPage')
def home(request):
    return render(request, 'TodoUI/index.html')





def register(request):
    if request.user.is_authenticated:
        return redirect('todoui:home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username =  form.cleaned_data.get('username')
                messages.success(request, 'La cuenta fue creada para ' + username)
                return redirect('todoui:loginPage')
        context= {'form': form}


        return render(request, 'TodoUI/register.html', context)


def loginPage(request):

    if request.user.is_authenticated:
        return redirect('todoui:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username= username, password=password )

            if user is not None:
                login(request, user)
                return redirect('todoui:home')
            else :
                messages.info(request, 'Usuario o contraseña son incorrectos')
                

        context= {}
        return render(request, 'TodoUI/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('todoui:loginPage')