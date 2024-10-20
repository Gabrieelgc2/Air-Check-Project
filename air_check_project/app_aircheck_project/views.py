from django.shortcuts import render

def home(request):
    return render(request, './usuarios/home.html')
def teste(request):
    return render(request, './usuarios/Airchecking.html')
def news(request):
    return render(request, './usuarios/news.html')
def about(request):
    return render(request, './usuarios/about.html')