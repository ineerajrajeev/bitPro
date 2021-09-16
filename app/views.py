from django.shortcuts import render, HttpResponse
from app.process import *

def index(request):
    context = {
        "ans": process(request)[0],
        "error": process(request)[1],
        "style": process(request)[2]
    }
    return render(request, 'index.html', context)
