from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse

from .forms import CreateUserForm, CreateProject
from django.contrib.auth.decorators import login_required

from .models import Graphs
from .templates.home.work import makegraph

#registration 
def registerView(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Acount was create for ' + user)
            return redirect('login')
    context = {'form': form}
    
    return render(request, 'registration/register.html', context)

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return redirect('work_zone')        
        else:
            messages.info(request, 'Username OR password is incorrect')
    context= {}
    return render(request, 'registration/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


#work zone
@login_required(login_url='login')
def workZone(request):
    form = CreateProject()
    if request.method == 'POST':
        form = CreateProject(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            #make graph
            x = [request.POST.get('x1'),request.POST.get('x2'),request.POST.get('x3'),request.POST.get('x4'),request.POST.get('x5')]
            y = [request.POST.get('y1'),request.POST.get('y2'),request.POST.get('y3'),request.POST.get('y4'),request.POST.get('y5')]
            
            makegraph(x, y)
        #delete all records
        if request.POST.get('delete'):
           Graphs.objects.all().delete()
        
    #lits graphs
    graphs = Graphs.objects.all()
    context={'form': form, 'graphs':graphs}

    return render(request, 'home/work_zone.html', context)

#index   
def index(request):
    return render(request, 'index.html')

#display example graphs
def graph1View(request):
    return render(request,'graphics/graph1.html')

def graph2View(request):
    return render(request,'graphics/graph2.html')

def graph3View(request):
    return render(request,'graphics/graph3.html')

def graph4View(request):
    return render(request,'graphics/graph4.html')