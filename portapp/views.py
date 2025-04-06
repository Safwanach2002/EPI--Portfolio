from django.shortcuts import render
from .models import Aboutsection, AboutsectionM, Service, ServiceM, Testimonial, TestimonialM

# Create your views here.

def home(request):
    return render(request, 'home.html')

def index(request):
    about = Aboutsection.objects.first()
    services = Service.objects.all()  # Fetch all service items
    testimonials = Testimonial.objects.all()

    return render(request, 'index.html', {
        'about': about,
        'services': services,
        'testimonials':testimonials,
    })

def indexM(request):
    aboutM = AboutsectionM.objects.first()
    servicesM = ServiceM.objects.all()  # Fetch all service items
    testimonialsM = TestimonialM.objects.all()

    return render(request, 'indexM.html', {
        'aboutM': aboutM,
        'servicesM': servicesM,
        'testimonialsM':testimonialsM,
    })


