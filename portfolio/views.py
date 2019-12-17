from django.shortcuts import render

def home(request):
    title = "Portfolio"
    
    return render(request, 'index.html',{'title':title})
