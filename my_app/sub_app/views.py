from django.shortcuts import render
from .forms import MyFrom

# Create your views here.
def home(request):
    form=MyFrom(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            form.save()
    return render(request, "home.html", {"form":form})