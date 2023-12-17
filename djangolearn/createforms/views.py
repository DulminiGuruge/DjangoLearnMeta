from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from createforms.forms import InputFrom

def form_view(request):
    form = InputFrom()
    context = {"form":form}
    return render(request, "home.html",context)
