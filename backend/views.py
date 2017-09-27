from django.shortcuts import render
from random import randint
from django.http import HttpResponse
import json
from .app import simulation


def index(request):
    """
    serving up the main app page which loads the Vue.js from WebPack
    """
    context = {
        'data': 'value',
    }
    return render(request, 'index.html', context)


def tick(request):

    positions = simulation.tickSim()

    objPos = []

    for x, column in enumerate(positions):
        for y, cell_value in enumerate(column):
            objPos.append({"x": x, "y": y, "n": cell_value})

    return HttpResponse(json.dumps(objPos), content_type="application/json")

def setup(request):
    simulation.genWorld()
    return HttpResponse(json.dumps("status: ok"), content_type="application/json")