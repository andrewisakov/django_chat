from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json
from .models import Room


# Create your views here.
@login_required
def index(request):
    rooms = Room.objects.order_by('title')
    return render(request, 'chat/index.html', {'rooms': rooms})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))})
