from django.shortcuts import render, redirect, reverse
from django.contrib import auth

# log in page for user
def login(request):
    return render(request, 'accounts/login.html')

# logout page for user
def logout(request):
    auth.logout(request)
    return redirect(reverse('index'))