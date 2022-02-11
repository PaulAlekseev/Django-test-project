from django.shortcuts import render

rooms = [
    {'id':1, 'name':"Lets learn python"},
    {'id':2, 'name':"Design with me"},
    {'id':2, 'name':"Backend developers"},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'main/home.html', context)


def room(request, pk):
    room = None
    for i in rooms:
        if i["id"] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'main/room.html', context)
