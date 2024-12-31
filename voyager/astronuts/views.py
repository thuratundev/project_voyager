from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Astronut

def astronuts(request):
    astronuts = Astronut.objects.all()
    template = loader.get_template('astronuts/index.html')
    context = {
        'astronuts': astronuts,
    }
    return render(request, 'astronuts/index.html', context)

# Create your views here.
