from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     template = loader.get_template('therapistApp/index.html')
#     context = {
#         'greeting': 'Hello Overlord!!',
#     }
#     return HttpResponse(template.render(context, request))

# Or we use a render
def index(request):
    context = {
        'greeting': 'Hello Overlord!!',
    }
    return render(request, 'therapistApp/index.html', context)


# Login view
def login(request):
    return render(request, 'therapistApp/login.html')


# Signup view
def signup(request):
    return render(request, 'therapistApp/signup.html')


# Dashboard view
def dashboard(request):
    return render(request, 'therapistApp/dashboard.html')