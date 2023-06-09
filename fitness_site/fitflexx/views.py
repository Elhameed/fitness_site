from django.shortcuts import render
from .models import Class

def index(request):
    return render(request, 'index.html')

def classes(request):
    # Retrieve the list of classes from the database
    class_list = Class.objects.all()
    
    # Pass the classes to the template
    return render(request, 'classes.html', {'classes': class_list})
