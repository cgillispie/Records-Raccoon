# app/drf_project/views.py

from django.http import JsonResponse, HttpResponse

def ping(request):
    data = {"ping": "pong!"}
    return JsonResponse(data)

def homepage(request):
    greeting = 'Hey! from the Records Raccoon!'
    return HttpResponse(greeting)