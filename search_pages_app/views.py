from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html');

def image_search(request):
    return render(request, 'google_image.html');

def advanced_search(request):
    return render(request, 'google_advanced.html');