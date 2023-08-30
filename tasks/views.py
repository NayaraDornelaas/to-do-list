from django.shortcuts import render
from django.http import HttpResponse

from .models import *
# Create your views here.

def index(request):
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    #a render function combines a template with a context dictionary and returns an HttpResponse object with the rendered text.
    return render(request, 'tasks/list.html', context)