from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
def skill(request):
    data = list(Skill.objects.values())
    return JsonResponse(data, safe=False)

def projects(request):
    data = list(Projects.objects.values())
    return JsonResponse(data, safe=False)

def experiences(request):
    data = list(Experiences.objects.values())
    return JsonResponse(data, safe=False)