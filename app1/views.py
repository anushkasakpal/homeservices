from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import userform
from .models import usermodel
from django.contrib.auth.decorators import login_required
from django.conf import settings



# Create your views here.
@login_required(login_url='log_url')
def adduser(request):
    form = userform()
    print(request, '>>>>>>>>>>>>')
    template_name = 'app1/user.html'
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            form.save()
            subject = 'welcome to Home Service!!!'
            message = f'Hi {form.cleaned_data.get("fname")} your appointment is booked.\ncontact details of {form.cleaned_data.get("services")}-8734827582\nThank you for using Home Service'
            email_from = 'HomeService@gmail.com'
            recipient_list = [form.cleaned_data.get("email")]
            send_mail(subject, message, email_from, recipient_list)
            return redirect('successful')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='adminlog')
def showView(request):
    data = usermodel.objects.all()
    template_name = 'app1/show.html'
    context = {'data': data}
    return render(request, template_name, context)


def updateView(request, pk):
    obj = usermodel.objects.get(id=pk)
    form = userform(instance=obj)
    if request.method == 'POST':
        form = userform(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show')
    template_name = 'app1/user.html'
    context = {'form': form}
    return render(request, template_name, context)


def deleteView(request, pk):
    template_name = 'app1/delete_confirm.html'
    obj = usermodel.objects.get(id = pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show')
    context = {'data': obj}
    return render(request, template_name, context)


def home(request):
    template_name = 'app1/home.html'
    return render(request,template_name)


@login_required(login_url='log_url')
def electrician(request):
    print(request, "<<<<<<<<<request")
    return redirect('showservicemen')


@login_required(login_url='log_url')
def plumber(request):
    return redirect('add')


@login_required(login_url='log_url')
def cleaner(request):
    return redirect('add')


@login_required(login_url='log_url')
def carpenter(request):
    return redirect('add')


@login_required(login_url='log_url')
def painter(request):
    return redirect('add')


@login_required(login_url='log_url')
def welder(request):
    return redirect('add')


def success(request):
    template_name = "app3/booksuccessfully.html"
    return render(request, template_name)


def aboutus(request):
    template_name = "app1/about.html"
    return render(request, template_name)


def contactus(request):
    template_name = "app1/contact.html"
    return render(request, template_name)