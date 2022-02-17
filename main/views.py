from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

def home(request):
    q = request.GET.get('q')
    if request.GET.get('q') != None:
        q = request.GET.get('q')
    else:
        q = ''

    rooms = Room.objects.filter(Q(topic__name__icontains=q)|
                                Q(name__icontains=q)|
                                Q(description__icontains=q)
                                )

    topics = Topic.objects.all()
    room_count = rooms.count()

    context = {'rooms': rooms, 'topics':topics, 'room_count': room_count}
    return render(request, 'main/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'main/room.html', context)


@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("Your not allowed here")

    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'main/room_form.html', context)


@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Your not allowed here")

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    return render(request, 'main/delete.html', {'obj': room})
