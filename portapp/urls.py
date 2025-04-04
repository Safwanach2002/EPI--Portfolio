from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('index/', views.index, name='index'),  # Default English page
    path('ml/', views.indexM, name='indexM'),  # Malayalam page
    path('en/', views.indexE, name='indexE'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
