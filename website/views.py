from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    return HttpResponse("This page contains information about the author")
