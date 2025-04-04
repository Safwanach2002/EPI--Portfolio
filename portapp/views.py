from django.shortcuts import render
from .models import ContentE,ContentM

# Create your views here.

def home(request):
    return render(request, 'home.html')

def indexE(request):
    contentE = ContentE.objects.all()
    return render(request, 'indexE.html', {'contentE': contentE})

def indexM(request):
    contentM = ContentM.objects.all()
    return render(request, 'indexM.html', {'contentM': contentM})

def index(request):
    return render(request, 'index.html')

