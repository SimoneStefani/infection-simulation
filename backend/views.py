from django.shortcuts import render
from random import randint
from django.http import HttpResponse
import json


def index(request):
    """
    serving up the main app page which loads the Vue.js from WebPack
    """
    context = {
        'data': 'value',
    }
    return render(request, 'index.html', context)


def tick(request):

    positions = []

    for i in range(0, 50):
        for j in range(0, 50):
            positions.append({"x": j, "y": i, "n": randint(0, 2)})

    return HttpResponse(json.dumps(positions), content_type="application/json")