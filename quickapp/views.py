from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def gallary(request):
    return render(request,'gallary.html')
def about(request):
    return render(request,'about.html')