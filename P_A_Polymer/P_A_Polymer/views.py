from django.http import JsonResponse, HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hello Testing!')
