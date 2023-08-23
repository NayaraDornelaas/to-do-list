from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #a render function combines a template with a context dictionary and returns an HttpResponse object with the rendered text.
    return render(request, 'tasks/list.html')