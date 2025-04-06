from django.db import models

class Aboutsection(models.Model):
    title = models.CharField(max_length=100,default="About Dominic")
    paragraph1=models.TextField()
    paragraph2=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='about_images/')
    
    def _str_(self):
        return self.title

class AboutsectionM(models.Model):
    title = models.CharField(max_length=100,default="About Dominic")
    paragraph1=models.TextField()
    paragraph2=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='about_images/')

    def _str_(self):
        return self.title

class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='icons/')
    description = models.TextField()

    def _str_(self):
        return self.title

class ServiceM(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='icons/')
    description = models.TextField()

    def _str_(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote_title = models.CharField(max_length=200)  # Like: "Wonderful Support!"
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    
    def _str_(self):
        return self.name

class TestimonialM(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    quote_title = models.CharField(max_length=200)  # Like: "Wonderful Support!"
    feedback = models.TextField()
    image = models.ImageField(upload_to='testimonials/')
    
    def _str_(self):
        return self.name
