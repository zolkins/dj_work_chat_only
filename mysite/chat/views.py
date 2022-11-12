# chat/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='index')
def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
