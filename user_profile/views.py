from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import Topic


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'topics':topics,
               'room_messages': room_messages}
    return render(request, 'user_profile/profile.html', context)