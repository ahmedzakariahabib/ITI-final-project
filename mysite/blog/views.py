from django.shortcuts import render

def index(request):
    return render(request, 'posts/index.html')
# Create your views here.
