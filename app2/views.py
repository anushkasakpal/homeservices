from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registerView(request):
    form = UserCreationForm()
    template_name = 'app2/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print('form save successfully')
            return redirect('log_url')
    context = {'form': form}
    return render(request, template_name, context)


def loginView(request):
    template_name = 'app2/log.html'
    context = {}
    if request.method == 'POST':
        u = request.POST.get('un')
        p = request.POST.get('pw')
        user = authenticate(username = u, password = p)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, template_name, context)


def logoutView(request):
    logout(request)
    return redirect('log')
