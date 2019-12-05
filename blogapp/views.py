from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def map(request):
    return render(request, 'kakaomap.html')

def mapsearch(request):
    return render(request, 'mapsearch.html')
