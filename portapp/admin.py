from django.contrib import admin

# Register your models here.
from .models import Aboutsection, Service,Testimonial
from .models import AboutsectionM, ServiceM,TestimonialM

admin.site.register(Aboutsection)
admin.site.register(Service)
admin.site.register(Testimonial)


admin.site.register(AboutsectionM)
admin.site.register(ServiceM)
admin.site.register(TestimonialM)