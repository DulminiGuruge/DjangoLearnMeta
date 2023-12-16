from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

def home(request):
    path = request.path
    return HttpResponse(path, content_type='text/html',charset='utf-8')


def menuitems(request,dish):
    items={
        'pasta':'with cheese',
        'falafel':'deep fried',
        'cheesecake':'dessert'
    }

    description=items[dish]

    return HttpResponse(f"<h2>{dish}</h2>"+description)

def drinks(request, drink_name):
    drink = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)


