from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Image

# Create your views here.
def home(request):
    formatted_time = timezone.now().strftime("%H:%M:%S.%f")
    context = {
        'current_time': formatted_time,
    }
    return render(request, 'images/home.html', context)

def index(request):
    context = {
        'images': Image.objects.all()
    }
    return render(request, 'images/index.html', context)