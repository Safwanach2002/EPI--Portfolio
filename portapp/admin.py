from django.contrib import admin

# Register your models here.
from .models import ContentE,ContentM

admin.site.register(ContentE)
admin.site.register(ContentM)