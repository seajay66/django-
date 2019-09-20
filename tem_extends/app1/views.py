from django.shortcuts import render

# Create your views here.
def backend(request):
    return render(request,"index.html")