from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        return redirect('register')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':
        return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
