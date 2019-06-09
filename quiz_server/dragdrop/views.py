from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "dragdrop/index.html")

def preview(request):
    return render(request, "admin/sometemplate.html")