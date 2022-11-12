from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# index page
def index(request):
    # if username in db
    if request.POST:
        # request.POST.get('username')
        # request.POST.get('password')

        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

        if user is not None:
            login(request, user)
            return redirect('chat/global')
        else:
            return register(request)
    else:
        return render(request, 'index.html')


# logout
def logoutUser(request):
    logout(request)
    return redirect('index')


# register page
def register(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {'form': form}  # pass form to template
    return render(request, 'register.html', context)


@login_required(login_url='index')
def chat(request):
    return redirect('chat/global')


@login_required(login_url='index')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
