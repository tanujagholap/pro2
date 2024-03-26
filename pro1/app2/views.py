from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



def login_view(request):
    template_name = 'app2/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('show_url')
        else:
            return HttpResponse('plz enter correct username or password')
    return render(request, template_name)



@login_required(login_url='login_url')
def logout_view(request):
    logout(request)
    return redirect('login_url')



def signup_view(request):
    template_name = 'app2/signup.html'
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Registered Successfully....')
    context = {'form': form}
    return render(request, template_name, context)


def cpass_view(request):
    template_name = 'app2/cpass.html'
    if request.method == 'POST':
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect('login_url')
    return render(request, template_name)

