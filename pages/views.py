from ast import Return
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "pages/index.html")
