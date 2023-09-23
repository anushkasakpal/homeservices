from django.shortcuts import render, redirect

from .forms import servicemenForm
from .models import adminmodel
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def addServicemen(request):
    form = servicemenForm()
    template_name = 'app3/servicemen.html'
    if request.method == 'POST':
        form = servicemenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showservicemen')
    context = {'form': form}
    return render(request, template_name, context)


def showServicemen(request):
    data1 = adminmodel.objects.all()
    template_name = 'app3/showservicemen.html'
    context = {'data': data1}
    return render(request, template_name, context)


def book(request):
    return redirect('add')


def cleaner(request):
    return redirect('add')


def carpenter(request):
    return redirect('add')


def painter(request):
    return redirect('add')


def welder(request):
    return redirect('add')


@login_required(login_url='log_url')
def showElectrician(request):
    data1 = adminmodel.objects.filter(service="electrician")
    template_name = 'app3/showservicemen.html'
    context = {'data': data1}
    return render(request, template_name, context)


@login_required(login_url='log_url')
def showPlumber(request):
    data1 = adminmodel.objects.filter(service="plumber")
    template_name = 'app3/showservicemen.html'
    context = {'data': data1}
    return render(request, template_name, context)


@login_required(login_url='log_url')
def showCleaner(request):
    data1 = adminmodel.objects.filter(service="cleaner")
    template_name = 'app3/showservicemen.html'
    context = {'data': data1}
    return render(request, template_name, context)


@login_required(login_url='log_url')
def showCarpenter(request):
    data1 = adminmodel.objects.filter(service="carpenter")
    template_name = 'app3/showservicemen.html'
    context = {'data': data1}
    return render(request, template_name, context)


@login_required(login_url='log_url')
def showPainter(request):
    data1 = adminmodel.objects.filter(service="painter")
    template_name = 'app3/showservicemen.html'
    context = {'data': data1}
    return render(request, template_name, context)


@login_required(login_url='log_url')
def showWelder(request):
    data1 = adminmodel.objects.filter(service="welder")
    template_name = 'app3/showservicemen.html'
    context = {'data': data1}
    return render(request, template_name, context)



# Create your views here.
def adminregisterView(request):
    form = UserCreationForm()
    template_name = 'app3/adminregister.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('form save successfully')
            return redirect('adminlog')
    context = {'form': form}
    return render(request, template_name, context)


def adminloginView(request):
    template_name = 'app3/adminlog.html'
    context = {}
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username = u, password = p)
        if user is not None:
            login(request, user)
            return redirect('show')
    return render(request, template_name, context)


def adminlogoutView(request):
    logout(request)
    return redirect('adminlog')
